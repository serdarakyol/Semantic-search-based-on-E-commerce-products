from fastapi import APIRouter

from recommendation_api.api.routes import routes_recommend

api_router = APIRouter()
api_router.include_router(routes_recommend.router, tags=["Recommendation"], prefix="/recommendation")
