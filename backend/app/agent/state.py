from typing import TypedDict, List, Dict

class AgentState(TypedDict):
    query: str
    properties: List[Dict]
    user_preferences: Dict
    user_email: str   