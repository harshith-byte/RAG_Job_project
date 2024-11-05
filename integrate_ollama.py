import ollama
from data_embedding import model
from store_embedding import index
from data_embedding import data
import numpy as np

client = ollama.Client()


def get_response(query):
    query_embedding = model.encode([query])
    distance, indices = index.search(np.array(query_embedding), k=100)  # Retrieve top 5 documents
    result = data.iloc[indices[0]].copy()
    return result[['title','description','occupation','employer_description','insertion_date']]
    # retrieved_docs = [data['description'].iloc[i] for i in indices[0]]
    # prompt = " ".join(retrieved_docs)
    # p = """
    #     for the given prompt - {query}, 
    #     use the data - {prompt} and give the details about the job openings. 
    #     list down the job opening with the following headlines
    #         1. title of the job 
    #         2. location of the job
    #         3. requirements
    #         4. benefits
    #         5. tasks
    #         if there are no similar job openings as per the {query} then repond back with no jobs available
    # """
    # response = client.generate(prompt=prompt, model='mistral')
    # return response