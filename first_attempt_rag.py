
from openai import OpenAI
import numpy as np
import os
from sklearn.metrics.pairwise import cosine_similarity

from dotenv import load_dotenv
load_dotenv("OPENAPIKEY")

OPENAI_API_KEY = os.getenv('OPENAPIKEY')

question = "2023年の第1事業部の売上はどのくらい？"
documents = [
    "2023年上期売上200億円, 下期売上300億円",
    "2023年第1事業部売上300億円, 第2事業部売上150億円, 第3事業部売上50億円", 
    "2024年は全社で1000億円の売上を目指す"
]

def vectorize_text(text):
    client = OpenAI(api_key=OPENAI_API_KEY)

    response = client.embeddings.create(
        input = text,
        model= "text-embedding-3-small"
    )

    # print(response)
    print(response.data[0].embedding)
    return response.data[0].embedding

vectors = [vectorize_text(doc) for doc in documents]
question_vector = vectorize_text(question)

# 類似度の判定
max_similarity = 0
most_similar_index = 0
for index, vector in enumerate(vectors):
    similarity = cosine_similarity([question_vector], [vectors])[0][0]
    if similarity > max_similarity:
        max_similarity = similarity
        most_similar_index = index

print(documents[most_similar_index])
