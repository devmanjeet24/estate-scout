from fastapi import APIRouter, Depends
from app.agent.graph import build_graph
from app.core.dependencies import get_current_user

router = APIRouter()

graph = build_graph()

@router.post("/run")
async def run_agent(query: str, user=Depends(get_current_user)):

    print("🔥 Agent started with query:", query)

    result = await graph.ainvoke({
        "query": query,
        "properties": [],
        "user_preferences": {}
    })

    print("✅ Agent finished")

    # ensure safe JSON response
    return result