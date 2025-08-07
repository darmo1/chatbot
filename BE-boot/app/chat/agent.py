from langgraph.graph import StateGraph, START, END
from app.chat.rag_node import ChatState, rag_node

# Construcción del grafo
def get_agent_graph():
    builder = StateGraph(ChatState)
    builder.add_node("rag_node", rag_node)
    builder.add_edge(START, "rag_node")
    builder.add_edge("rag_node", END)
    return builder.compile()
