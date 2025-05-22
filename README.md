# Health Retriever Plugin for Dify

A dual-path retrieval plugin that provides health QA and personalized product recommendations.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Start Qdrant:
```bash
docker run -p 6333:6333 qdrant/qdrant
```

3. Start Ollama with deepseek-llm:7b:
```bash
ollama run deepseek-llm:7b
```

4. Build the indices:
```bash
python scripts/build_qdrant_index.py
```

5. Run the API:
```bash
python app.py
```

## Usage

Send POST requests to `/retrieve` endpoint with:
```json
{
    "query": "What are the risks of high blood pressure?",
    "user_id": "user123"
}
```
