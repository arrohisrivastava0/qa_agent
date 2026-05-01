from langgraph.graph import StateGraph, END
from typing import TypedDict, List
from agents.retriever_agent import retriever_agent
from agents.analyst_agent import analyst_agent
from agents.reporter_agent import reporter_agent

class AgentState(TypedDict):
    query: str
    retrieved_context: str
    analysis: str
    report: str
    agent_logs: List[str]

def build_graph():
    graph = StateGraph(AgentState)

    graph.add_node("retriever", retriever_agent)
    graph.add_node("analyst", analyst_agent)
    graph.add_node("reporter", reporter_agent)

    graph.set_entry_point("retriever")
    graph.add_edge("retriever", "analyst")
    graph.add_edge("analyst", "reporter")
    graph.add_edge("reporter", END)

    return graph.compile()