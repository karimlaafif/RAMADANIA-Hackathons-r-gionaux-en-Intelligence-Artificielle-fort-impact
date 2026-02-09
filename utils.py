import os
from typing import List
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from dotenv import load_dotenv

load_dotenv()

# Constants
DATA_DIR = "data"
PERSIST_DIR = "chroma_db"
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

class SmartCivicRAG:
    def __init__(self):
        """Initialize the RAG system with embeddings and vector store."""
        print("Loading embeddings model...")
        self.embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
        
        # Check if vector store exists, otherwise create it
        if os.path.exists(PERSIST_DIR) and os.listdir(PERSIST_DIR):
            print("Loading existing vector store...")
            self.vector_store = Chroma(
                persist_directory=PERSIST_DIR, 
                embedding_function=self.embeddings
            )
        else:
            print("Creating new vector store from data...")
            self.create_vector_store()
            
        self.retriever = self.vector_store.as_retriever(
            search_type="similarity",
            search_kwargs={"k": 3}
        )

    def create_vector_store(self):
        """Load documents from data directory and create vector store."""
        if not os.path.exists(DATA_DIR):
            os.makedirs(DATA_DIR)
            return

        loader = DirectoryLoader(DATA_DIR, glob="**/*.md", loader_cls=TextLoader, show_progress=True)
        docs = loader.load()
        
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50
        )
        splits = text_splitter.split_documents(docs)
        
        self.vector_store = Chroma.from_documents(
            documents=splits, 
            embedding=self.embeddings,
            persist_directory=PERSIST_DIR
        )
        print("Vector store created and persisted.")

    def get_response(self, query: str, language: str = "English"):
        """
        Generate a response using RAG.
        If OpenAI API key is missing, returns a mock response based on retrieval.
        """
        
        # Retrieve relevant context
        retrieved_docs = self.retriever.invoke(query)
        context_text = "\n\n".join([doc.page_content for doc in retrieved_docs])
        
        # System Prompt
        system_template = """You are 'Musa'id', an expert AI assistant for Moroccan Public Services.
        Use the following pieces of retrieved context to answer the user's question.
        
        If the answer is not in the context, say "I don't have that information right now" (translate this to the target language).
        Do NOT hallucinate. Keep answers simple, step-by-step, and clear.
        
        Respond entirely in {language}.
        
        Context:
        {context}
        """
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", system_template),
            ("human", "{question}")
        ])

        # Check for OpenAI Key
        api_key = os.getenv("OPENAI_API_KEY")
        
        if api_key:
            llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
            chain = (
                {"context": lambda x: context_text, "question": RunnablePassthrough(), "language": lambda x: language}
                | prompt
                | llm
                | StrOutputParser()
            )
            return chain.invoke(query)
        else:
            # Fallback if no API key is present (Mocking the LLM generation for demo purposes)
            return f"""[System Note: INTENT DETECTED -> RAG RETRIEVAL SUCCESSFUL]
            
            **(Simulated LLM Response in {language})**
            
            Based on your query '{query}', here is the information found:
            
            {context_text[:500]}...
            
            *(To get full AI generation, please set OPENAI_API_KEY in .env)*
            """

if __name__ == "__main__":
    # Test the system
    rag = SmartCivicRAG()
    print(rag.get_response("How to renew CIN?", "English"))
