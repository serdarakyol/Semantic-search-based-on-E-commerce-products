from pydantic import BaseModel
from typing import List

from pydantic.types import Json

class RecommendationRequest(BaseModel):
    product_names: List

class RecommendationResponse(BaseModel):
    cart: List
    similar_items: List