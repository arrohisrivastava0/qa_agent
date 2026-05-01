```markdown
# Multi-Agent Financial Assistant

A multi-agent pipeline for enterprise financial analysis using LangGraph, LangChain, and Groq (Llama 3.1). Three specialized AI agents collaborate in sequence to retrieve context, perform financial reasoning, and generate structured reports — mimicking real-world enterprise financial workflows.

## Architecture

User Query → Retriever Agent → Analyst Agent → Reporter Agent → Structured Report

Each agent is a specialized LLM node in a LangGraph state graph:
- **Retriever Agent** — Identifies key financial entities, metrics, and time periods from the query
- **Analyst Agent** — Performs financial reasoning, calculates metrics, identifies trends and anomalies
- **Reporter Agent** — Generates a structured business report with executive summary, key findings, and recommendations

## Tech Stack

- **LangGraph** — Agent orchestration and state graph management
- **LangChain** — LLM abstraction and message formatting
- **Groq (Llama 3.1 8B)** — Fast LLM inference backend
- **FastAPI** — REST API serving
- **Uvicorn** — ASGI server
- **Python-dotenv** — Environment variable management

## Project Structure

multi-agent-financial-assistant/
├── agents/
│   ├── retriever_agent.py   # Entity and context extraction
│   ├── analyst_agent.py     # Financial reasoning and metric calculation
│   └── reporter_agent.py    # Structured report generation
├── graph.py                 # LangGraph state graph definition
├── main.py                  # FastAPI application
├── requirements.txt
└── .env                     # API keys (not committed)

## Setup

git clone https://github.com/arrohisrivastava0/qa_agent.git
cd qa_agent
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

Create a `.env` file in the root directory:

GROQ_API_KEY=your_groq_api_key_here

Get a free API key at https://console.groq.com

## Running the API

uvicorn main:app --reload

Server starts at http://127.0.0.1:8000

## Usage

curl -X POST http://127.0.0.1:8000/analyze \
  -H "Content-Type: application/json" \
  -d '{"query": "What are the cost reduction opportunities in Q4 enterprise spending?"}'

## Sample Output

{
  "query": "What are the cost reduction opportunities in Q4 enterprise spending?",
  "report": "Financial Report: Cost Reduction Opportunities in Q4 Enterprise Spending. Executive Summary: ...",
  "agent_logs": [
    "[Retriever] Identified key entities from query",
    "[Analyst] Completed financial reasoning",
    "[Reporter] Generated final report"
  ]
}

## Why This Matters

Enterprise applications like SAP S/4HANA deal with large volumes of financial data across controlling and cost management modules. This project demonstrates how multi-agent LLM pipelines can automate financial analysis workflows — reducing manual effort and surfacing actionable insights from unstructured financial queries.
```