from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from dotenv import load_dotenv
import os
load_dotenv()
credential_path="path"
os.environ['GOOGLE_APPLICATION_CREDENTIALS']=credential_path

pdf_path=Path(__file__).parent / "node-handbook.pdf"

loader=PyPDFLoader(file_path=pdf_path)

docs=loader.load()


text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

texts = text_splitter.split_documents(documents=docs)

print(texts)
#create embeddings

embeddings = GoogleGenerativeAIEmbeddings(
    
    model="models/embedding-001",
    api_key=credential_path
 )

"""
client = genai.Client(api_key=apiKey)
embeddings=client.models.embed_content(
        model="gemini-embedding-exp-03-07")

"""

"""
vector_store=QdrantVectorStore.from_documents(
    documents=[],
    url="http://localhost:6333/",
    collection_name="learning_langchain",
    embedding=embeddings

)

vector_store.add_documents(documents=texts)
"""
print("Injection done")


retreiver=QdrantVectorStore.from_existing_collection(
    url="http://localhost:6333/",
    collection_name="learning_langchain",
    embedding=embeddings

)

search_result=retreiver.similarity_search(

    query="What is FS module?"
)

print("relevant chuks:",search_result)

SYSTEM_PROMPT=f"""You are an helpful assistant who responds on the basis of available context.

Context:{search_result}


"""

