from fastapi import APIRouter, Depends
from motor.motor_asyncio import AsyncIOMotorClient

from app.utils.mongodb import get_database
from app.models.users import UserInResponse


router = APIRouter()


@router.get("/", response_model=UserInResponse, tags=["users"])
async def get_all_users(db: AsyncIOMotorClient = Depends(get_database)) -> UserInResponse:
    """
    Get a list of users in the database

    Each item will have a set of params
    """
    users = []
    rows = db["core"]["users"].find()
    async for row in rows:
        users.append(row)
    return UserInResponse(users=users)



@router.get("/{item_id}")
async def read_item(item_id: str):
    return {"name": "Fake Specific Item", "item_id": item_id}
