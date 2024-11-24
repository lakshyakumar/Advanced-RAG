from langchain_core.tools import tool
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.graph import StateGraph, MessagesState, START, END
from langgraph.prebuilt import ToolNode
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.vectorstores import InMemoryVectorStore
from dotenv import load_dotenv

load_dotenv()

system_prompt = (
    "You are an assistant for question-answering tasks. "
    "You can call the tool get_info to get information about Lakshya. "
    "try to break input in simpler questions and execute all of them to get simpler queries"
    "tool takes input as {input: str} and returns a list of chunks. "
    "If you find the answer with get_info, reply based on that. "
    "Otherwise, just say 'I don't know the answer'. "
    "Answer elaboratively."
)

# Load and split the document
file_path = "./assets/LakshyaKumarCV.pdf"
loader = PyPDFLoader(file_path)
docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=100)
splits = text_splitter.split_documents(docs)

# Create a vector store and retriever
vectorstore = InMemoryVectorStore.from_documents(
    documents=splits, embedding=OpenAIEmbeddings()
)
retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 5})

# Define the tool for retrieving information
@tool
def get_info(input) -> int:
    """Retrieve information about Lakshya."""
    chunks = retriever.invoke(input)
    return chunks

# Initialize the model and parser
model = ChatOpenAI(model="gpt-4")
parser = StrOutputParser()
model_with_tools = model.bind_tools([get_info])

# Define the tool node
tool_node = ToolNode([get_info])

# Define the workflow functions
def should_continue(state: MessagesState):
    last_message = state["messages"][-1]
    return "tools" if last_message.tool_calls else END

def call_model(state: MessagesState):
    response = model_with_tools.invoke(state["messages"])
    return {"messages": [response]}

# Set up the workflow
workflow = StateGraph(MessagesState)
workflow.add_node("agent", call_model)
workflow.add_node("tools", tool_node)
workflow.add_edge(START, "agent")
workflow.add_conditional_edges("agent", should_continue, ["tools", END])
workflow.add_edge("tools", "agent")

# Compile and run the application
app = workflow.compile()


while True:
    user_input = input("\nUser: ")
    if user_input.lower() in ["quit", "exit", "q"]:
        print("Goodbye!")
        break

    try:
        for chunk in app.stream(
                {"messages": [("system", system_prompt), ("human", user_input)]}, stream_mode="values"
            ):
            chunk["messages"][-1].pretty_print()
    except Exception as e:
        print(f"An error occurred: {e}")
        