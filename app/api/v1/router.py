from fastapi import APIRouter
from app.api.v1.endpoints import skin

api_router = APIRouter()
api_router.include_router(skin.router, prefix="/skin", tags=["Skin Analysis"])