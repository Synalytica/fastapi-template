from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def read_items():
    """
    Read a list of items.

    Each item will have a set of params
    - **name**: Item name
    """
    return [{"name": "Item Foo"}, {"name": "item Bar"}]


@router.get("/{item_id}")
async def read_item(item_id: str):
    return {"name": "Fake Specific Item", "item_id": item_id}
