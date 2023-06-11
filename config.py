import dotenv
import os
import sys

dotenv.load_dotenv('.env')

# Config
openai_key = os.environ.get('OPENAI_KEY')
model_embedding_name = os.environ.get('OPENAI_EMBEDDING_MODEL')
pinecone_key = os.environ.get('PINECONE_KEY')
pinecone_index_name = os.environ.get('PINECONE_INDEX')
pinecone_env = os.environ.get('PINECONE_ENV')
pinecone_namespace = str(sys.argv[1]) or ''