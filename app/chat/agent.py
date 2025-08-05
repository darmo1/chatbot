from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.graph import StateGraph, START, END
from typing import TypedDict
import os
from dotenv import load_dotenv

# Cargar configuración
load_dotenv()
os.environ.setdefault("HUGGINGFACEHUB_API_TOKEN", os.getenv("HUGGINGFACEHUB_API_TOKEN", ""))

# Configurar LLM
llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1-0528",
    task="text-generation",
    max_new_tokens=50,
    do_sample=False,
    repetition_penalty=1.03,
    provider="auto",
)

chat_model = ChatHuggingFace(llm=llm)
system_message = SystemMessage(content="You are a helpful assistant. Answer the user's questions...")

# Estado tipado
class _State(TypedDict):
    message: str

# Nodo de procesamiento
def node_llm_huggingface(state: _State) -> _State:
    user_text = state["message"]
    ai_msg_obj = chat_model.invoke([system_message, HumanMessage(content=user_text)])
    return {"message": ai_msg_obj.content}

# Construcción del grafo
def get_agent_graph():
    builder = StateGraph(_State)
    builder.add_node("node_llm", node_llm_huggingface)
    builder.add_edge(START, "node_llm")
    builder.add_edge("node_llm", END)
    return builder.compile()
