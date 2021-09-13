from fastapi import APIRouter

from recommendation_api.utils import clean_text

api_router = APIRouter()
api_router.include_router(clean_text.router, tags=[
                          "preprocessing"], prefix="/preprocessing")
