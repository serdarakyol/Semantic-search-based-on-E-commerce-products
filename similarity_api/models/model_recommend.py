from pydantic import BaseModel
from typing import List

class SimilarityRequest(BaseModel):
    product_names: List

class SimilarityResponse(BaseModel):
    cart: List
    similar_items: List