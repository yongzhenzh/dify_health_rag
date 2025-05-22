import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import json
from embedding import EmbeddingModel
from qdrant_client import QdrantClient

def build_indices():
    # Initialize components
    embedding_model = EmbeddingModel()
    qdrant = QdrantClient()
    
    # Load and index QA data
    with open("data/health_qa.json") as f:
        qa_data = json.load(f)
    
    # Load and index product data
    with open("data/products.json") as f:
        product_data = json.load(f)
        
    # Build indices...

if __name__ == "__main__":
    build_indices()
