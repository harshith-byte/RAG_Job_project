import faiss
from data_embedding import embeddings
import numpy as np

embedding_matrix = np.array(embeddings)
dimension = embedding_matrix.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embedding_matrix)
