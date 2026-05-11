# Enterprise Knowledge Assistant

A multi-agent LLM pipeline built with LangGraph for enterprise financial document Q&A. Three specialized agents — retriever, analyst, and reporter — collaborate through a stateful graph to process queries end-to-end and return structured reports.

## Architecture

```
Query → [Retriever Agent] → [Analyst Agent] → [Reporter Agent] → Structured Report
              ↓                    ↓                   ↓
       Entity extraction    Financial reasoning    Executive summary
       & context building   & trend analysis       Key findings
                                                   Recommendations
```

Built with LangGraph's `StateGraph` for inter-agent state management. Each agent reads from and writes to a shared `AgentState`, passing structured context through the pipeline.

Supports **LangSmith tracing** for prompt observability and agent workflow debugging — set `LANGSMITH_API_KEY` in `.env` to activate.

## Tech Stack

- **LangGraph** — agent orchestration via StateGraph
- **LangChain + Groq** — LLM inference (LLaMA 3.1)
- **FastAPI** — REST API serving

- **LangSmith** — prompt tracing and observability (optional)

## Setup

```bash
git clone https://github.com/arrohisrivastava0/qa_agent.git
cd qa_agent
pip install -r requirements.txt

cp .env.example .env
# Add your GROQ_API_KEY to .env
uvicorn main:app --reload
```

## API Usage

**POST** `/analyze`

```json
{
  "query": "What were the revenue trends for Q3 2024?"
}
```

**Response**

```json
{
  "query": "What were the revenue trends for Q3 2024?",
  "report": "## Executive Summary\n...\n## Key Findings\n...\n## Recommendations\n...",
  "agent_logs": [
    "[Retriever] Identified key entities from query",
    "[Analyst] Completed financial reasoning",
    "[Reporter] Generated final report"
  ]
}
```

## Project Structure

```
qa_agent/
├── main.py              # FastAPI app + LangSmith tracing setup
├── graph.py             # LangGraph StateGraph definition
├── agents/
│   ├── retriever_agent.py   # Entity extraction & context retrieval
│   ├── analyst_agent.py     # Financial reasoning & analysis
│   └── reporter_agent.py    # Structured report generation
├── requirements.txt
└── .env.example
```
