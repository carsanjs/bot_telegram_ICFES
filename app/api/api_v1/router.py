from fastapi import APIRouter
from api.endpoint import icfes

router = APIRouter()

router.include_router(
    icfes.icfes_router,
    prefix='/icfes',
    tags=['icfes'],
    responses={
        404: {
            "description": "Not found"
        }
    }
)