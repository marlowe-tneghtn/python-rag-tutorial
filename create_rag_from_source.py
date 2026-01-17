import requests
from bs4 import BeautifulSoup
from openai import OpenAI
import numpy as np
import os
from sklearn.metrics.pairwise import cosine_similarity

from dotenv import load_dotenv
load_dotenv()

OPENAPIKEY = os.environ("OPENAPIKEY")

# ######
# ソースとなるページの情報をスクレイピングして、
# 必要な情報のみに選別して、
# 適切な形に整形して、ラグとして必要な情報を生成する
# ######

url = ""
response = requests.get(url)
# HTML形式で取得する
soup = BeautifulSoup(response.text, "html.parser")
# ページ内の全てのdivタグを取得
text_nodes = soup.find_all("div")
# print(text_nodes)

# 1つの文章にページのテキスト情報をまとめる
joined_text = "".join(t.text.replace("\t", "").replace("\n", "") for t in text_nodes)
# t_all = []
# for t in text_nodes:
#     # print(t.text)
#     t_all.append(t.text.replace("\t", "").replace("\n", ""))

# joined_text = ",".join(t_all)

# ##########
# 適切な形でDBに登録するには？
# ##########

# 考え方: 100文字区切りかつ分割部分に重複するものを残すことで、
# 文脈を崩さずにLLMに情報を渡すことができる

# 1chunk = 400文字
# chunkごとの重複文字数 = 50文字
chunk_size = 400
overlap = 50
chunks = []
start = 0

while start + chunk_size <= len(joined_text):
    chunks.append(joined_text[start: start + chunk_size])
    start += (chunk_size - overlap)

if start < len(joined_text):
    chunks.append(joined_text[-chunk_size:])


# ソースから取得した情報を元に、LLMからの回答を受ける
