from pydantic import BaseModel
from typing import List

from pydantic.types import Json

class SimilarityRequest(BaseModel):
    product_names: List

class SimilarityResponse(BaseModel):
    cart: List
    similar_items: List