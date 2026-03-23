from fastapi import APIRouter, Depends
from app.schemas.property_schema import Property
from app.services.property_service import create_property, get_all_properties
from app.core.dependencies import get_current_user

router = APIRouter()


@router.post("/")
async def add_property(
    property_data: Property,
    user=Depends(get_current_user)
):
    return await create_property(property_data, user["email"])


@router.get("/")
async def list_properties(
    user=Depends(get_current_user)
):
    return await get_all_properties(user["email"])