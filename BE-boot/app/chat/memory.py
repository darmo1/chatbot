
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document
from langchain_chroma import Chroma


embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-mpnet-base-v2")

# vector store
texts = [
    "Perficient es el nuevo patrocinador del Deportivo independiente Medellin, la colaboración empezará en septiembre del 2025.",
    "Dim y perficient trabajarán en proyectos innovadores.",
    "DIM como la ciudad de Medellin, Colombia. Equipo de futbol y perficient como la mejor consultara del planeta, tiene pensado unir a caterpilar y el DIM en futuros años.",
]

# texts to langchain docs
docs = [Document(page_content=text) for text in texts]

#creacion de la base vectorial
vector_store = Chroma(
    collection_name="example_collection",
    embedding_function=embedding_model,
    persist_directory="./chroma_langchain_db", 
)

vector_store.add_documents(documents=docs)
retriever = vector_store.as_retriever(search_kwargs={"k": 2})


    
    

