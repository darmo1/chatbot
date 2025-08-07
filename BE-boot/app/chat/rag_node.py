from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.messages import SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from app.chat.memory import  retriever
from typing import TypedDict
import os
from dotenv import load_dotenv

# Cargar configuración
load_dotenv()
os.environ.setdefault("HUGGINGFACEHUB_API_TOKEN", os.getenv("HUGGINGFACEHUB_API_TOKEN", ""))

# LLM config
llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1-0528",
    task="conversational",
    max_new_tokens=100,
    do_sample=False,
    repetition_penalty=1.03,
    provider="auto",
)

chat_model = ChatHuggingFace(llm=llm)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Answer the user's questions using the context below if available, and add emoticons in you answer. :\n\n{context}"),
        ("user", "{input}"),
    ]
)

combine_docs_chain = create_stuff_documents_chain(chat_model, prompt)
# RAG setup
rag_chain = create_retrieval_chain(retriever=retriever, combine_docs_chain=combine_docs_chain)

# Typed state
class ChatState(TypedDict):
    message: str

# RAG Node
def rag_node(state: ChatState) -> ChatState:
    query = state["message"]
    rag_result = rag_chain.invoke({"input": query})
 
    return {"message": rag_result["answer"],}
    
