from langchain.document_loaders import CSVLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.vectorstores import Chroma


loader = CSVLoader(file_path="disease_ontology.csv", encoding = 'utf-8')
documents = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
chunks = text_splitter.split_documents(documents)
embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2") 
vectorstore = Chroma.from_documents(chunks, embeddings, persist_directory="./chroma_db")
