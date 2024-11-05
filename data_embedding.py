from sentence_transformers import SentenceTransformer
from data_preparation_app import *
import pandas as pd
model = SentenceTransformer('all-MiniLM-L6-v2')

data= data_cleaning()


data['embeddings'] = data['description'].apply(lambda x: model.encode(x))
embeddings = data['embeddings'].tolist()