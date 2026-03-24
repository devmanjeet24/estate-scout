from fastapi import APIRouter, Depends
from app.core.dependencies import get_current_user
from app.core.llm import get_llm

router = APIRouter()

@router.post("/")
async def chat(query: str, user=Depends(get_current_user)):
    llm = get_llm()

    prompt = f"""
You are a smart real estate assistant.

User: {query}

Rules:
- If greeting → ask what property they want
- If clear property query → reply: "Searching properties..."
- Keep it short
"""

    res = llm.invoke(prompt).content

    return {"response": res}