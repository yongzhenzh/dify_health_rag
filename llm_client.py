import requests
from typing import Dict

class OllamaClient:
    def __init__(self):
        self.base_url = "http://localhost:11434/api/generate"
        self.model = "deepseek-llm:7b"
        
    def generate_answer(self, query: str, context: str, user_profile: Dict) -> str:
        prompt = f"""Based on the user profile:
{user_profile}

And the following health information:
{context}

Please answer the user's question:
{query}

Provide a concise and accurate answer focusing on the most relevant information."""

        response = requests.post(
            self.base_url,
            json={
                "model": self.model,
                "prompt": prompt,
                "stream": False
            }
        )
        

        resp_json = response.json()
        print("LLM raw response:", resp_json)

        if "response" in resp_json:
            return resp_json["response"]
        elif "error" in resp_json:
            raise Exception(f"LLM error: {resp_json['error']}")
        else:
            raise Exception(f"Unexpected LLM response: {resp_json}")
