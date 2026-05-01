from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from graph import build_graph

load_dotenv()

app = FastAPI(title="Multi-Agent Financial Assistant")
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
    return {"status": "Multi-Agent Financial Assistant running"}