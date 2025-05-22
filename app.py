from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

from embedding import EmbeddingModel
from my_qdrant_client import QdrantClient
from db_utils import get_user_profile
from llm_client import OllamaClient

app = FastAPI()

class QueryRequest(BaseModel):
    query: str
    user_id: str

class ProductRecommendation(BaseModel):
    id: str
    name: str
    description: str
    score: float

class QueryResponse(BaseModel):
    answer: str
    recommendations: List[ProductRecommendation]

# Initialize components
embedding_model = EmbeddingModel()
qdrant_client = QdrantClient()
llm_client = OllamaClient()

@app.post("/retrieve", response_model=QueryResponse)
async def retrieve(request: QueryRequest):
    # Get user profile
    user_profile = get_user_profile(request.user_id)
    
    # Embed query
    query_embedding = embedding_model.embed(request.query)
    
    # Dual path retrieval
    # qa_results = qdrant_client.search_qa(query_embedding)
    # product_results = qdrant_client.search_products(query_embedding, user_profile)
    
    # Generate answer using LLM
    context = ""
    answer = llm_client.generate_answer(request.query, context, user_profile)
    
    # Format product recommendations
    # recommendations = [
    #     ProductRecommendation(
    #         id=p.id,
    #         name=p.name,
    #         description=p.description,
    #         score=p.score
    #     ) for p in product_results
    # ]
    recommendations = []

    return QueryResponse(answer=answer, recommendations=recommendations)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
