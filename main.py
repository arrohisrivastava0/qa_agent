import os
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from graph import build_graph

load_dotenv()

if os.getenv("LANGSMITH_API_KEY"):
    os.environ["LANGCHAIN_TRACING_V2"] = "true"
    os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT", "enterprise-knowledge-assistant")

app = FastAPI(title="Enterprise Knowledge Assistant")

graph = build_graph()

class QueryRequest(BaseModel):
    query: str

@app.post("/analyze")
def analyze(request: QueryRequest):
    result = graph.invoke({
        "query": request.query,
        "retrieved_context": "",
        "analysis": "",
        "report": "",
        "agent_logs": []
    })
    return {
        "query": request.query,
        "report": result["report"],
        "agent_logs": result["agent_logs"]
    }

@app.get("/")
def root():
    return {"status": "Enterprise Knowledge Assistant running"}