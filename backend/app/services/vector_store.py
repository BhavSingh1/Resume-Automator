import faiss
import numpy as np

class VectorStore:
    def __init__(self, dimension: int):
        self.index = faiss.IndexFlatL2(dimension)
        self.snippet_ids = []

    def add(self, embedding: list[float], snippet_id: int):
        vec = np.array([embedding]).astype("float32")
        self.index.add(vec)
        self.snippet_ids.append(snippet_id)

    def search(self, query_embedding: list[float], k=5):
        q = np.array([query_embedding]).astype("float32")
        distances, indices = self.index.search(q, k)
        return [self.snippet_ids[i] for i in indices[0]]
