from pathlib import Path

from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Pinecone
from langchain.document_loaders import TextLoader, PyPDFLoader
import pinecone
from config import *

chunk_size = 1000
chunk_overlap = 200

# OpenAI Embeds
embeddings = OpenAIEmbeddings(
    model=model_embedding_name,
    openai_api_key=openai_key
)

# Pinecone Vector DB
pinecone.init(
    api_key=pinecone_key,
    environment=pinecone_env
)

# Generate chunks
# Create Embeds
# pathList = list(Path("documents/").glob("**/*.md"))
pathList = list(Path("documents/").glob("**/*.pdf"))

print("Found "+ str(len(pathList)) + " documents")

text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)

documents = []
for path in pathList:
    # document = TextLoader(str(path)).load()
    document = PyPDFLoader(str(path)).load()
    documentChunks = text_splitter.split_documents(document)
    for k, v in enumerate(documentChunks):
        documents.append(v)

print("Chunk size:", str(chunk_size))
print("Chunk overlap:", str(chunk_overlap))
print("Generated Chunks:", len(documents))

# Store vectors
Pinecone.from_documents(documents, embeddings, index_name=pinecone_index_name, namespace=pinecone_namespace)
