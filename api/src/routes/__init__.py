from fastapi import APIRouter
from .api import userRouter

router = APIRouter()

router.include_router(userRouter)
