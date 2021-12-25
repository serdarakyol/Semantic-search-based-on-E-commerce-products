from fastapi import APIRouter

from recommendation_api.api.routes import recommend

api_router = APIRouter()
api_router.include_router(recommend.router, tags=["Recommendation"], prefix="/recommendation")
