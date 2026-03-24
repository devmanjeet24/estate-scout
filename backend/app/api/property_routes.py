from fastapi import APIRouter, Depends
from app.services.property_service import (
    get_all_properties,
    get_property_by_id,
    delete_property,
    update_property
)
from app.core.dependencies import get_current_user

router = APIRouter()

@router.get("/")
async def list_properties(user=Depends(get_current_user)):
    return await get_all_properties(user["email"])


@router.get("/{property_id}")
async def get_property(property_id: str, user=Depends(get_current_user)):
    return await get_property_by_id(property_id)


@router.delete("/{property_id}")
async def delete(property_id: str, user=Depends(get_current_user)):
    return await delete_property(property_id)


@router.put("/{property_id}")
async def update(property_id: str, data: dict, user=Depends(get_current_user)):
    return await update_property(property_id, data)