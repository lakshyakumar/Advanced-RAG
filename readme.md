# Advanced Rag with LangRaph and RAG tool

This project is an AI-powered assistant for question-answering tasks. It uses RAG tool and models to retrieve and process information from a PDF document.

## Table of Contents

- Difference Between Advanced RAG and Normal RAG
- AI Question Refactoring and Subdivision, with example
- Installation
- Usage
- Project Structure
- Contributing
- License

## Difference Between Advanced RAG and Normal RAG

**Normal RAG (Retrieval-Augmented Generation):**

- Combines retrieval and generation models.
- Retrieves relevant documents from a knowledge base.
- Generates answers based on the retrieved documents.
- Typically uses a single retrieval step followed by a generation step.

**Advanced RAG:**

- Enhances the basic RAG framework with additional features.
- May include multiple retrieval steps to refine the search results.
- Incorporates conditional logic to handle complex queries.
- Utilizes advanced techniques like re-ranking and filtering to improve answer quality.
- Can integrate with external tools and APIs for more comprehensive information retrieval.

## AI Question Refactoring and Subdivision

In this project, the AI can refactor and subdivide complex questions into simpler sub-questions. It then calls the RAG tools with these sub-questions and appropriate prompts to provide a comprehensive answer.

### Example

If you prompt the AI with:

```
User: Tell me about Lakshya's experience, projects, and education.
```

The AI will refactor this into three sub-questions:

1. What is Lakshya's experience?
2. What are Lakshya's projects?
3. What is Lakshya's education?

The AI then calls the RAG tools with these sub-questions and combines the responses to provide an elaborate answer:

```
Lakshya has nearly 6 years of experience in the field of blockchain, cloud, and full-stack solutions. His roles have included working as a full-stack developer, a blockchain and DevOps engineer, and most recently as a web3 solution architect and team lead for a fund tokenization project. During his tenure, he has worked with numerous clients and technologies, including NodeJS, ReactJS, Hyperledger fabric, and Hyperledger Besu.

Regarding projects, Lakshya has worked on a number of them, including:
1. Hyperledger/bevel - An accelerator that aids developers in setting up and deploying a production-ready DLT network.
2. Turbulent - A React.js and Next.js hook library for blockchain interface, available on NPM.
3. Enthalpy - A react UI kit available on NPM.
4. Taming the Ethereum Jungle: Wallact Makes Smart Contracts Your Plaything - A project involving Ethereum smart contracts.
5. Worked on creating Ripple APIs for banking clients.

As for his education, he holds a Bachelor of Technology (BTech) degree from Delhi Technological University (DTU, Delhi) obtained in 2015. He also has a Master of Technology (MTech) degree in Computational Mathematics from the National Institute of Technology (NIT), Surathkal, Karnataka which he earned between 2016 and 2018.
```

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/lakshyakumar/advanced-rag.git
   cd your-repo
   ```

2. Create and activate a virtual environment:

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:

   ```sh
   pip install -r requirements.txt
   ```

4. Create a `.env` file based on the `env.sample` file and fill in the necessary environment variables.

## Usage

1. Run the main script:

   ```sh
   python main.py
   ```

2. Interact with the assistant by typing your questions. To exit, type `quit`, `exit`, or `q`.

## Project Structure

- `main.py`: The main script that sets up and runs the assistant.
- `assets/`: Directory containing the PDF document to be processed.
- `requirements.txt`: List of dependencies required for the project.
- `venv/`: Virtual environment directory.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
