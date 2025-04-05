from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
import pandas as pd


script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "data", "cleaned_dadjokes.csv")

df = pd.read_csv(csv_path)
embeddings = OllamaEmbeddings(model="mxbai-embed-large")

db_location = "./chroma_langchain_db"
add_documents = not os.path.exists(db_location)

if add_documents:
  documents = []
  ids = []

  for i, row in df.iterrows():
    document = Document(
      page_content = row['dadjoke'],
      metadata={"upvotes": row['upvotes']},
      id=str(i)
    )

    ids.append(str(i))
    documents.append(document)

vector_store = Chroma(
  collection_name = "dad-jokes",
  persist_directory = db_location,
  embedding_function = embeddings
)

if add_documents:
  vector_store.add_documents(documents = documents, ids = ids)

retriever = vector_store.as_retriever(
  search_kwargs = {"k": 5}
)