from fastapi import APIRouter

icfes_router = APIRouter()

@icfes_router.get("/icfes")
async def get_icfes():
    return {"message": "Hello World"}