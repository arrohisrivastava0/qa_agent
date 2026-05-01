from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage

llm = ChatGroq(model="llama-3.1-8b-instant")

def reporter_agent(state: dict) -> dict:
    query = state["query"]
    analysis = state["analysis"]
    
    messages = [
        SystemMessage(content="""You are a financial report writer for enterprise 
        applications. Given an analysis, generate a concise, structured report 
        with: Executive Summary, Key Findings, and Recommendations. 
        Format it clearly for business stakeholders."""),
        HumanMessage(content=f"Original Query: {query}\n\nAnalysis: {analysis}")
    ]
    
    response = llm.invoke(messages)
    
    return {
        **state,
        "report": response.content,
        "agent_logs": state.get("agent_logs", []) + [f"[Reporter] Generated final report"]
    }