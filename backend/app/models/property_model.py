def property_model(property) -> dict:
    return {
        "id": str(property["_id"]),
        "title": property["title"],
        "price": property["price"],
        "address": property["address"],
        "description": property.get("description", ""),
        "image": property.get("image", ""),
        "folder": property.get("folder", "")
    }