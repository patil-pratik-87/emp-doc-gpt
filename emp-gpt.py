# importing all the required libraries
import sys
import os
from dotenv import load_dotenv, find_dotenv
from langchain_community.chat_models import ChatOpenAI
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnableLambda
from langchain_core.vectorstores import VectorStoreRetriever
from langchain.memory import ConversationBufferMemory, ConversationSummaryBufferMemory
from langchain import hub
from langchain.chains import RetrievalQA
from typing import Optional, List
from langchain.text_splitter import MarkdownHeaderTextSplitter
import nest_asyncio
from llama_index.core.schema import Document
from langchain_chroma import Chroma
import chromadb
from uuid import uuid4

from flask import Flask, request, jsonify,logging
from flask_cors import CORS

nest_asyncio.apply()
import configparser

# Global properties to be configured from a properties file

# Initialize the global properties
config = configparser.ConfigParser()
config.read('config.ini')

# Define global properties
OPENAI_MODEL = config.get('OpenAI', 'model', fallback='gpt-4o-mini')
EMBEDDING_MODEL = config.get('OpenAI', 'embedding_model', fallback='text-embedding-3-large')
ROOT_DIR = config.get('Paths', 'root_dir', fallback='./docs')
CHROMA_DB_DIR = config.get('Paths', 'chroma_db_dir', fallback='./emp_chroma_db')
VERBOSE = config.getboolean('Debug', 'verbose', fallback=False)
MAX_TOKENS = config.getint('Hyperparameters', 'max_tokens', fallback=4096)
TEMPERATURE = config.getfloat('Hyperparameters', 'temperature', fallback=1)
SEARCH_TYPE = config.get('Hyperparameters', 'search_type', fallback='mmr')
SEARCH_K = config.getint('Hyperparameters', 'search_k', fallback=4)
FETCH_K = config.getint('Hyperparameters', 'fetch_k', fallback=8)
CHAIN_TYPE = config.get('Hyperparameters', 'chain_type', fallback='stuff')
RECREATE_EMBEDDINGS = config.getboolean('Actions', 'recreate_embeddings', fallback=False)

print("Verbose : ", VERBOSE)

if VERBOSE:
    print(f"""Initial Properties \n
        OPENAI_MODEL: {OPENAI_MODEL} \n
        EMBEDDING_MODEL: {EMBEDDING_MODEL} \n
        ROOT_DIR: {ROOT_DIR} \n
        CHROMA_DB_DIR: {CHROMA_DB_DIR} \n
        VERBOSE: {VERBOSE} \n
        MAX_TOKENS: {MAX_TOKENS} \n
        TEMPERATURE: {TEMPERATURE} \n
        SEARCH_TYPE: {SEARCH_TYPE} \n 
        SEARCH_K: {SEARCH_K} \n
        FETCH_K: {FETCH_K} \n
        CHAIN_TYPE: {CHAIN_TYPE} \n
        RECREATE_EMBEDDINGS: {RECREATE_EMBEDDINGS} \n
        """
    )

# Global variables
chain = None
llm = None

# Function to reload properties (can be called if properties need to be updated at runtime)
def reload_properties():
    config.read('config.properties')
    global OPENAI_MODEL, EMBEDDING_MODEL, ROOT_DIR, VERBOSE, MAX_TOKENS, TEMPERATURE, SEARCH_TYPE, SEARCH_K, FETCH_K, CHAIN_TYPE, CHROMA_DB_DIR , RECREATE_EMBEDDINGS
    OPENAI_MODEL = config.get('OpenAI', 'model', fallback='gpt-4o-mini')
    EMBEDDING_MODEL = config.get('OpenAI', 'embedding_model', fallback='text-embedding-3-large')
    ROOT_DIR = config.get('Paths', 'root_dir', fallback='./docs')
    CHROMA_DB_DIR = config.get('Paths', 'chroma_db_dir', fallback='./emp_chroma_db')
    VERBOSE = config.getboolean('Debug', 'verbose', fallback=False)
    MAX_TOKENS = config.getint('HYPERPARAMETERS', 'max_tokens', fallback=4096)
    TEMPERATURE = config.getfloat('HYPERPARAMETERS', 'temperature', fallback=0.7)
    SEARCH_TYPE = config.get('HYPERPARAMETERS', 'search_type', fallback='mmr')
    SEARCH_K = config.getint('HYPERPARAMETERS', 'search_k', fallback=4)
    FETCH_K = config.getint('HYPERPARAMETERS', 'fetch_k', fallback=8)
    CHAIN_TYPE = config.get('HYPERPARAMETERS', 'chain_type', fallback='stuff')
    RECREATE_EMBEDDINGS = config.getboolean('ACTIONS', 'RECREATE_EMBEDDINGS', fallback=False)

    if VERBOSE:
        print("Reloading properties \n")

def init_env():
# Add the root directory to sys.path
# Loading all the keys
    def load_env():
        _ = load_dotenv(find_dotenv())

    def get_openai_api_key():
        load_env()
        openai_api_key = os.getenv("OPENAI_API_KEY")
        return openai_api_key
    
    root_dir = os.path.abspath(os.path.join(os.getcwd(), '..'))
    sys.path.append(root_dir)
    os.environ['OPENAI_API_KEY'] = get_openai_api_key()


def load_llm():
    global llm
    llm =  ChatOpenAI(model=OPENAI_MODEL, temperature=TEMPERATURE)

def get_system_prompt() -> str:
    return """
Role:
You are an expert support assistant for EMP (Elastic Machine Pools), helping users—ranging from first-time users to experienced \
    system admins and DevOps personnel navigate, understand, and troubleshoot the product.

Task:
Provide accurate, and structured(rules given below in point no 7 later) responses to the queries of the users based on the below rules. Please  do  not explicitly list the thought process headers.

Guidelines for Responses:
	1.Initial Understanding and Topic Identification:
	•	First, identify the core aspects of the user’s query. Think through what the user is really asking. What 1-2 main search topics or key concepts are most relevant?
	
    2.Topic Breakdown and Explanation:
	•	After identifying the key topics, provide a concise and clear explanation of each one. Summarize each key concept and their relation(if any) that will help the user better understand EMP, AWS EKS, and how they relate to cost savings.
	•	Think: “What does the user need to know to understand this topic fully?”
	•	Think: "Have I already covered these topics in the above conversation?" If yes, then do not repeat.
	
    3.Answer the Core Query:
	•	After helping the user grasp the necessary concepts, think about the precise question the user has asked. What is the most direct and concise answer to their question? Avoid unnecessary details, and focus on clarity and brevity.
	•	Think: “What’s the best way to answer this query succinctly while making sure the user understands the core of the solution?”
	
    4.Provide Step-by-Step Instructions:
	•	Now that the user understands the main concepts, think through the procedure they need to follow. Guide them with detailed, step-by-step instructions on how to configure or the above key topis in the application.
	•	Consider the user’s experience level. If they are new, explain each step in greater detail. For seasoned users, focus on efficiency.
	•	If this procedure has already been discussed in the history, acknowledge that, and only provide new information or further details.
	
    5.	Identify and Mention Gotchas or Caveats:
	•	Before finishing the response, think about any common issues or pitfalls that could arise when implementing the instructions. Include these gotchas or caveats to ensure the user is prepared for potential challenges.
	•	Again, check the conversation history to avoid repeating information that’s already been mentioned.
    
    6. Generate a 1-2 line summary of the response, which captures the essence of the response in a concise manner.

	7.	Structured and Readable Output:
	•	Organize your response logically using HTML tags for readability:
	•	<h1> for main headings
	•	<h2> for subheadings
	•	<p> for text
	•	<ul> and <li> for lists
	•	<strong> or <b> for emphases or hightlighting important information
	•	<a href="#"> for hyperlinks
	•	Ensure clean, readable HTML code by avoiding unnecessary newlines between tags.
    
	Finally, combine the above points  into a single coherent reponse for the user query.
    Let's now welcome the user and start the conversation.
"""

def get_user_prompt() -> str:
    return  """
Given a chat history and the latest user query \
which might reference context in the chat history,\
answer the user query.
The user query is : "{query}"
The chat history is : "{chat_history}"
"""

#  Split using the ***MarkdownHeaderTextSplitter*** and store its embeddings for all the docs(Optional, if already done)
def split_docs_using_md_header_splitter(root_dir="./docs", verbose=False)-> List[Document]:
    """
    Split the markdown files in the given directory into smaller Document objects.
    """
    all_documents = []
    headers_to_split_on = [
        ("#", "Markdown Header 1"),
        ("##", "Markdown Header 2"),
    ]    
    md_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on)
    # Walk through the directory and process each markdown file
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith(".md"):  # Process only markdown files
                file_path = os.path.join(dirpath, filename)
                with open(file_path, 'r', encoding='utf-8') as file:
                    if verbose:
                        print(f"Reading file ->{file_path}")
                    file_content = file.read()
                    documents = md_splitter.split_text(file_content)
                    all_documents.extend(documents)  
    if VERBOSE:
        print(f"Total {len(all_documents)} documents created")                    
    return all_documents

# Create embeddings for the given documents and store them in the Chroma DB
def create_embeddings(documents: List[Document], collection_name="emp-docs-collection", chroma_db_dir=CHROMA_DB_DIR, embedding_model=EMBEDDING_MODEL) -> List[Document]:
    """
    Create embeddings for the given documents.

        Args:
        documents (List[Document]): A list of documents to create embeddings for.
        collection_name (str): The name of the collection to store the embeddings in.

    Returns:
        List[Document]: A list of documents with the embeddings.
    """
    # Create a Chroma client
    client = chromadb.PersistentClient(path=chroma_db_dir)

    # Initialize the OpenAI embeddings model
    embeddings = OpenAIEmbeddings(model=embedding_model)


    vector_store = Chroma(
        client=client,
        collection_name=collection_name,
        embedding_function=embeddings,
        collection_metadata={"hnsw:space": "cosine"} # l2 is the default
    )
    # Add the documents to the vector store
    uuids = [str(uuid4()) for _ in range(len(documents))]
    ids = vector_store.add_documents(documents=documents, ids=uuids)
    if VERBOSE:
        print(f" {len(ids)} Documents added to the vector store successfully \n")
    return ids

# Split the docs and store the embeddings in the Chroma DB
def split_docs_and_store_embeddings(root_dir=ROOT_DIR, chroma_db_dir=CHROMA_DB_DIR)-> List[Document]:
    """
    Split the markdown files in the given directory into smaller Document objects.

    Args:
        root_dir (str): The root directory containing the markdown files.
        verbose (bool): If True, print the file path as it is read.

    Returns:
        List[Document]: A list of documents, each representing a split part of the original markdown files.
    """
    documents = split_docs_using_md_header_splitter(root_dir=root_dir)
    embeddings = create_embeddings(documents=documents, collection_name="emp-docs-collection")
    if VERBOSE:
        print(f" {len(embeddings)} Embeddings created and stored in the vector store successfully \n")
    return embeddings

# # Get the retriever for the given collection name from the Chroma DB
# def get_retriever(collection_name="emp-docs-collection", chroma_db_dir=CHROMA_DB_DIR, search_type=SEARCH_TYPE, search_kwargs={"k": SEARCH_K, "fetch_k": FETCH_K}) -> VectorStoreRetriever:
#     """
#     Get the vector store for the given collection name.
#     search_type: "mmr" or "similarity"
#     search_kwargs: dictionary of search parameters
#     Returns:
#         VectorStoreRetriever: A retriever object that can be used to retrieve documents from the vector store.
#     """
#     retreiver = Chroma(
#         client=client,
#         collection_name=collection_name,
#         embedding_function=OpenAIEmbeddings(model=EMBEDDING_MODEL)).as_retriever(search_type=search_type, search_kwargs=search_kwargs)
#     if VERBOSE:
#      print(f"Chroma DB instantiated and retreiver created with search type: {search_type} and search kwargs: {search_kwargs} \n")  
#     return retreiver
        

def get_retreival_qa_chain(collection_name="emp-docs-collection", 
                           chroma_db_dir=CHROMA_DB_DIR, 
                           embedding_model=EMBEDDING_MODEL,
                           search_type=SEARCH_TYPE, 
                           search_kwargs={"k": SEARCH_K, "fetch_k": FETCH_K}):
    """
    Get the LangChain chain for the given args
    Args:
        collection_name: name of the collection in the Chroma DB
        chroma_db_dir: directory of the Chroma DB
        search_type: "mmr" or "similarity"
        search_kwargs: dictionary of search parameters
    Returns:
        LangChain chain
    """
    client = chromadb.PersistentClient(path=chroma_db_dir)
    embeddings = OpenAIEmbeddings(model=embedding_model)
    vector_store = Chroma(
        client=client,
        collection_name=collection_name,
        embedding_function=embeddings)
    
    retriever = vector_store.as_retriever(search_type=search_type, search_kwargs=search_kwargs)
    
    memory = ConversationSummaryBufferMemory( memory_key="chat_history", llm=llm, max_token_limit=2048, return_messages=True)

    chain =  RetrievalQA.from_chain_type(
        llm=llm, 
        chain_type=CHAIN_TYPE, 
        retriever=retriever,
        verbose=VERBOSE,
        memory=memory
    )

    # print("Retreiver And Retreival QA Chain created: \n", retriever.invoke("what is EMP?"))
    return chain;

def stripExtraSpaces(query):
    return query.replace("\\n", "").replace("\n", "")

def ask_query(query: str):
    prompt_template = ChatPromptTemplate.from_messages(
        [
            ("system", get_system_prompt()),
            MessagesPlaceholder("chat_history"),
            ("human", "Query :{query}. Let's think step by step.."),
        ]
    )
    result = chain.invoke(prompt_template.format(query=query, chat_history=chain.memory.chat_memory.messages))

    if VERBOSE:
        print(f"Result of the query {query} is : {result} \n")
    return stripExtraSpaces(result['result'])

def init():
    global chain
    reload_properties()
    init_env()
    load_llm()
    if RECREATE_EMBEDDINGS:
        if VERBOSE:
            print("Recreating embeddings.. \n")
        split_docs_and_store_embeddings()
    if chain == None:
        chain = get_retreival_qa_chain()

init()

# Initialize the Flask application
app = Flask(__name__)
# Disable CORS by allowing all origins, methods, and headers
CORS(app, resources={r"/*": {"origins": "*"}})

# Define a route for the default URL, which will serve as a simple hello world endpoint
@app.route('/init')
def init():
    try:
        # Clear the memory of the chain, to avoid duplicate system prompts
        if VERBOSE:
            print("Clearing the memory of the chain \n")
        chain.memory.clear()

        prompt_template = ChatPromptTemplate.from_messages([
        ("system", get_system_prompt()),
        ])

        query =  prompt_template.format()
        print(f"System Prompt: {query}")
        response = chain.invoke(query)
        print(f"Response: {response}")
        
        return response['result'] 
    except Exception as e:
        # logging.error("An error occurred", exc_info=True)
        return jsonify({"error": e}), 500

@app.route('/chat', methods=['GET'])
def chatbot():
    try:
        # Get the 'query' parameter from the URL
        query = request.args.get('query')
        if not query:
            return jsonify({"error": "Query parameter is missing"}), 400
        
        if VERBOSE:
            print(f"User asked: {query}")
        response = ask_query(query)
        
        if VERBOSE:
         print(f"Response: {response}")
         print(f"Memory: {chain.memory.buffer}")
        return jsonify({"response": response})
    except Exception as e:
        # logging.error("An error occurred", exc_info=True)
        return jsonify({"error": e}), 500


# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)



