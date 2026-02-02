from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

def create_faiss_index(chunks):
    """Create FAISS vectorstore from document chunks"""
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    
    return FAISS.from_texts(
        texts=chunks,
        embedding=embeddings
    )

from langchain_pinecone import PineconeVectorStore
from app.config import PINECONE_INDEX_NAME
import os

def create_pinecone_index(chunks):
    """Create Pinecone vectorstore from document chunks"""
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    
    # Ensure API key is set
    if not os.getenv("PINECONE_API_KEY"):
        raise ValueError("PINECONE_API_KEY environment variable is not set")
        
    return PineconeVectorStore.from_texts(
        texts=chunks,
        embedding=embeddings,
        index_name=PINECONE_INDEX_NAME
    )

def retrieve_similar_documents(vectorstore, query, k=4):
    """Retrieve similar documents from vectorstore"""
    return vectorstore.similarity_search(query, k=k)

