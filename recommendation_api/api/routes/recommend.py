from fastapi import APIRouter, Depends
from starlette.requests import Request

from recommendation_api.core import security
from recommendation_api.models.recommend import RecommendationResponse, RecommendationRequest
from recommendation_api.services.recommend import Recommend

router = APIRouter()

@router.post("/recommend", response_model=RecommendationResponse, name="recommend")
def post_recommend(
    request: Request,
    authenticated: bool = Depends(security.validate_request),
    request_data: RecommendationRequest = None,
) -> RecommendationResponse:

    recommend_service = Recommend()
    response_data = recommend_service.recommend(request_data)

    return response_data