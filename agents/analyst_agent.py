from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage

llm = ChatGroq(model="llama-3.1-8b-instant")

def analyst_agent(state: dict) -> dict:
    query = state["query"]
    context = state["retrieved_context"]
    
    messages = [
        SystemMessage(content="""You are a financial analyst specializing in 
        enterprise financial data. Given a query and retrieved context, perform 
        financial reasoning: calculate metrics, identify trends, flag anomalies, 
        and draw conclusions. Be precise and quantitative where possible."""),
        HumanMessage(content=f"Query: {query}\n\nContext: {context}")
    ]
    
    response = llm.invoke(messages)
    
    return {
        **state,
        "analysis": response.content,
        "agent_logs": state.get("agent_logs", []) + [f"[Analyst] Completed financial reasoning"]
    }