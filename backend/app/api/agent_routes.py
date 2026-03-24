from fastapi import APIRouter, Depends, BackgroundTasks, HTTPException
from app.core.dependencies import get_current_user
from app.agent.graph import build_graph
from app.db.database import db
import asyncio

router = APIRouter()

graph = None


def run_graph_task(state):
    try:
        asyncio.run(graph.ainvoke(state))
    except Exception as e:
        print("❌ AGENT ERROR:", str(e))


@router.post("/run")
async def run_agent(
    query: str,
    background_tasks: BackgroundTasks,
    user=Depends(get_current_user)
):
    global graph

    try:
        if graph is None:
            graph = build_graph()

        db_user = await db.users.find_one({"email": user["email"]})

        prefs = db_user.get("preferences", {})

        state = {
            "query": query,
            "properties": [],
            "user_preferences": prefs,
            "user_email": user["email"]
        }

        background_tasks.add_task(run_graph_task, state)

        return {
            "message": "Agent started",
            "status": "processing"
        }

    except Exception as e:
        print("❌ ROUTE ERROR:", str(e))
        raise HTTPException(status_code=500, detail="Agent failed")