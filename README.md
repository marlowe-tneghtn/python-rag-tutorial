# Python RAG Tutorial
Udemy講座「[【初心者向け】大規模言語モデルにおけるRAGを実装できるようになろう！Webページの情報を元に回答できるAIを作ろう！](https://www.udemy.com/course/rag-deploy/learn/lecture/43637386)」hands-on

## 参考講座
Udemy - 大規模言語モデルを活用する上で非常に重要なアプローチであるRAGについて学び実装していきます！特定のWebページの情報を元に回答してくれるAIを作っていきますよ！

### 対象
- Python初心者：Pythonの基本的な構文も説明している
- Pythonでのデータ分析初心者：Pythonのライブラリを使用したデータ分析の基礎を解説している
- 大規模言語モデルの生成AIの初心者：どういったものなのか、どんな背景があるのか＋公開されているLLMとRAGを使った基本的な仕組み・実装について解説している
※細かいところまで踏み込んだ内容というよりも、手を動かしつつＬＬＭやＲＡＧの知識の導入を学べるイメージ

### 注意事項
- APIキーの使用には、OpenAIのアカウントでクレジットを購入する必要があります。以下参考<br>
[API Keys取得ページ](https://platform.openai.com/settings/organization/api-keys)<br>
※講座受講時（2025/04/28）：最低5ドルのクレジットの購入が必要<br>
[OpenAI料金](https://openai.com/ja-JP/api/pricing/)<br>
※chatGPTのアカウントとは別


## 開発環境構築
### 前提
- Pythonがインストールされていること(仮想環境は任意)
### 手順
1. 本プロジェクトのソースをクローン
2. 以下のコマンドを使用し、ライブラリをインストール
```bash
pip install -r requirements.txt
```
3. [API Keys取得ページ](https://platform.openai.com/settings/organization/api-keys)から、APIキーを取得する<br>
※アカウントがない場合は作成から、APIの使用には課金が必要
4. .envファイルを新たに作成し、以下の記述を追加する
```.env
OPENAPIKEY="取得したAPIキー"
```
※「取得したAPIキー」には実際のキーを入力する
