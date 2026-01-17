import pandas as pd
import seaborn as sns


df = sns.load_dataset("titanic")

print(df) # DataFrame: 2次元（テーブルデータ）
print(df.head()) # 始めの5件
print(df.head(3)) # 始めの3件指定
print(df.shape) # 次元数情報
print(df.info()) # DataFrame内基本情報
print(df.columns) # カラム一覧
print(df["pclass"]) # Series: 1次元（ベクトルデータ）
print(df[["pclass"]])  # DataFrame: 2次元（テーブルデータ）
print(df["pclass"].unique()) # カラム値重複削除
print(df["pclass"].nunique()) # カラム重複削除後の数
print(df.iloc[0]) # 0行目取得
print(df.iloc[0:3]) # 0~2行目取得
print(df.describe()) # 統計
print(df.select_dtypes(include="number")) # カラムが"number"のもののみ取得
print(df.select_dtypes(include="number").groupby(df["survived"]).mean()) # カラムが"number"のもの中で、"survived"をキーにして平均値を取得
print(df.select_dtypes(include="number").groupby(df["survived"]).mean()["age"]) # カラムが"number"のもの中で、"survived"をキーにして"age"カラムの平均値を取得
print(df.sort_values("age")) # "age"カラムをキーにして並び替え(昇順)
print(df.sort_values("age", ascending=False)) # "age"カラムをキーにして並び替え(降順)

print(df.isnull().sum()) #それぞれのカラムでnullの合計数を取得
print(df.dropna()) # 欠損値がある行は削除
print(df["age"].fillna(0)) # 欠損値を0で補完
print(df["age"].fillna(df["age"].mean())) # 欠損値をカラムの平均値で補完

print(df.select_dtypes(include="number").corr()) # それぞれのカラムの相関関係

print(df.reset_index(names="index")) # indexの振り直し
df = df.reset_index(names="index")
df_a = df[["index", "survived"]]
df_b = df[["index", "pclass"]]
pd.merge(df_a, df_b, on="index", how="inner") # indexをキーにしてinner join
pd.concat([df_a, df_b], axis=1) # 横に結合
pd.concat([df_a, df_b], axis=0) # 縦に結合

df_sample = pd.read_csv("./sample.csv") # ファイルの読み込み
print(df_sample)

new_column = pd.Series(["man", "woman"])
df_sample["gender"] = new_column

df_sample.to_csv("df_sample2.csv") # ファイル出力