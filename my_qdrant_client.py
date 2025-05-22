from qdrant_client import QdrantClient as Qdrant
from typing import List, Dict

class QdrantClient:
    def __init__(self):
        self.client = Qdrant(host="localhost", port=6333)
        self.qa_collection = "health_qa"
        self.products_collection = "products"
        
    def search_qa(self, query_vector: List[float], limit: int = 5):
        results = self.client.search(
            collection_name=self.qa_collection,
            query_vector=query_vector,
            limit=limit
        )
        return results
        
    def search_products(self, query_vector: List[float], user_profile: Dict, limit: int = 3):
        # Add user profile based filtering
        results = self.client.search(
            collection_name=self.products_collection,
            query_vector=query_vector,
            limit=limit
        )
        return results
