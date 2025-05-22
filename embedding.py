from transformers import AutoModel, AutoTokenizer
import torch

class EmbeddingModel:
    def __init__(self):
        self.model_name = "BAAI/bge-m3"
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModel.from_pretrained(self.model_name)
        
    def embed(self, text: str) -> list[float]:
        inputs = self.tokenizer(text, return_tensors="pt", max_length=512, truncation=True)
        with torch.no_grad():
            embeddings = self.model(**inputs).last_hidden_state[:, 0, :].numpy()
        return embeddings[0].tolist()
