import requests
from bs4 import BeautifulSoup
from openai import OpenAI
import numpy as np
import os
from sklearn.metrics.pairwise import cosine_similarity

from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.environ("OPENAPIKEY")

# ######
# ソースとなるページの情報をスクレイピングして、
# 必要な情報のみに選別して、
# 適切な形に整形して、ラグとして必要な情報を生成する
# ######
def scrape_article(url):
    response = requests.get(url)
    # HTML形式で取得する
    soup = BeautifulSoup(response.text, "html.parser")
    # ページ内の全てのdivタグを取得
    text_nodes = soup.find_all("div")
    # print(text_nodes)

    # 1つの文章にページのテキスト情報をまとめる
    joined_text = "".join(t.text.replace("\t", "").replace("\n", "") for t in text_nodes)

    return joined_text


# ##########
# 適切な形でDBに登録するには？

# 考え方: 100文字区切りかつ分割部分に重複するものを残すことで、
# 文脈を崩さずにLLMに情報を渡すことができる

# 1chunk = 400文字
# chunkごとの重複文字数 = 50文字
# ##########
def chunk_text(text, chunk_size, overlap):
    chunks = []
    start = 0

    while start + chunk_size <= len(joined_text):
        chunks.append(joined_text[start: start + chunk_size])
        start += (chunk_size - overlap)

    if start < len(joined_text):
        chunks.append(joined_text[-chunk_size:])
    
    return chunks


# ##########
# RAGとして使用する情報をベクトル化
# ##########
def vectorize_text(text):
    client = OpenAI(api_key=OPENAI_API_KEY)

    response = client.embeddings.create(
        input = text,
        model= "text-embedding-3-small"
    )

    # print(response)
    # print(response.data[0].embedding)
    return response.data[0].embedding


# ##########
# 類似度の判定
# ##########
def find_most_similar(question_vector, vectors, documents):
    similarities = []

    for index, vector in enumerate(vectors):
        similarity = cosine_similarity([question_vector], [vector])[0][0]
        similarities.append([similarity, index])
    
    similarities.sort(reverse=True, key=lambda x: x[0])
    top_documents = [documents[index] for similarity, index in similarities[:2]]

    return top_documents
    
    # ↓ 類似度の高い1つを取得する場合
    # max_similarity = 0
    # most_similar_index = 0
    # for index, vector in enumerate(vectors):
    #     similarity = cosine_similarity([question_vector], [vectors])[0][0]
    #     if similarity > max_similarity:
    #         max_similarity = similarity
    #         most_similar_index = index

    # # print(documents[most_similar_index])
    # return documents[most_similar_index]


# ##########
# ソースから取得した情報を元に、LLMからの回答を受ける
# ##########
def ask_question(question, document):
    client = OpenAI(api_key=OPENAI_API_KEY)
    prompt = f'''以下の質問に以下の情報をベースにして答えてください。
    [ユーザの質問]
    {question}

    [情報]
    {document}
    '''

    response = client.completions.create(
        model="gpt-3.5-turbo",
        prompt=prompt,
        max_tokens=200
    )

    # print(prompt)
    # print(response.choices[0].text)

    return response.choices[0].text


def main():
    # RAGとして必要な情報を取得する
    url = "https://toukei-lab.com/achademy/?page_id=1619"
    article_texts = scrape_article(url)

    # 使用できる情報に整形する
    chunk_size = 400
    overlap = 50
    chunked_texts = chunk_text(article_texts, chunk_size, overlap)

    # 情報をベクトル化する
    question = "オーダーメイドプランの価格はいくらですか？"
    question_vector = vectorize_text(question)
    vectors = [vectorize_text(chunk) for chunk in chunked_texts]

    # 類似度の判定
    most_similar_documents = find_most_similar(question_vector, vectors, chunked_texts)

    # 回答の生成
    answer = ask_question(question, most_similar_documents)

    # 質問と回答の表示
    print(f"question: {question}")
    print(f"answer: {answer}")


if __init__ == '__main__' :
    main()