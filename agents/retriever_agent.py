from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage

llm = ChatGroq(model="llama-3.1-8b-instant")

def retriever_agent(state: dict) -> dict:
    query = state["query"]
    
    messages = [
        SystemMessage(content="""You are a financial document retrieval specialist. 
        Given a query, extract and identify the key financial entities, metrics, 
        and time periods being asked about. Return a structured summary of what 
        data needs to be retrieved."""),
        HumanMessage(content=f"Query: {query}")
    ]
    
    response = llm.invoke(messages)
    
    return {
        **state,
        "retrieved_context": response.content,
        "agent_logs": state.get("agent_logs", []) + [f"[Retriever] Identified key entities from query"]
    }