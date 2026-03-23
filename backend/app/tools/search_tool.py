from tavily import TavilyClient
from app.core.config import settings

client = TavilyClient(api_key=settings.TAVILY_API_KEY)

def search_properties(query: str):
    response = client.search(
        query=query,
        search_depth="advanced",
        max_results=3
    )

    results = []

    for r in response["results"]:
        results.append({
            "title": r.get("title"),
            "address": r.get("url"),
            "description": r.get("content"),
            "price": "unknown"
        })

    return results