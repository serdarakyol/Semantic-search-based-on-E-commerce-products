from fastapi import APIRouter, Depends
from starlette.requests import Request

from similarity_api.core import security
from similarity_api.models.model_recommend import SimilarityRequest, SimilarityResponse
from similarity_api.services.service_recommend import Recommend

router = APIRouter()

@router.post("/similar", response_model=SimilarityResponse, name="similar")
def post_recommend(
    request: Request,
    authenticated: bool = Depends(security.validate_request),
    request_data: SimilarityRequest = None,
) -> SimilarityResponse:

    recommend_service = Recommend()
    response_data = recommend_service.recommend(request_data)

    return response_data