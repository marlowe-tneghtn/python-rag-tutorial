import first_attempt_rag as far

prompt = f'''以下の質問に以下の情報をベースにして答えてください。
[ユーザの質問]
{far.question}

[情報]
{far.documents[far.most_similar_index]}
'''

response = far.client.completions.create(
    model="gpt-3.5-turbo",
    prompt=prompt,
    max_tokens=200
)

print(response.choices[0].text)