from fastapi import APIRouter

from similarity_api.api.routes import routes_similarity

api_router = APIRouter()
api_router.include_router(routes_similarity.router, tags=["Similarity"], prefix="/similarity")
