def user_model(user) -> dict:
    return {
        "id": str(user["_id"]),
        "email": user["email"],
        "preferences": user.get("preferences", {})
    }