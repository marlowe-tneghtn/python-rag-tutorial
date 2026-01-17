# Matplotlib: 可視化ライブラリ

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset("titanic")

# ヒストグラフ
# plt.hist(df["fare"], bins=40, range=[0, 100])
# plt.show()

# 折れ線グラフ
# plt.figure(figsize=(20,5))
# plt.plot(df["fare"])
# plt.title("titanic data")
# plt.xlabel("data_index")
# plt.ylabel("fare")
# plt.show()

# 
# df["fare"].hist(by=df["sex"])
# plt.show()

# 複数グラフ
# fig, axes = plt.subplots(2, 2, figsize=(20, 10))
# axes[0][0].hist(df["age"], bins=20)
# axes[0][1].hist(df["fare"], bins=20)
# axes[0][1].set_xlim(0, 200)
# axes[1][0].hist(df["sex"], bins=20)
# axes[1][1].hist(df["pclass"], bins=20)
# plt.show()

# 棒グラフ
# print(df.groupby("pclass").count())
# print(df.groupby("pclass").count()["survived"])
# plt.bar(df.groupby("pclass").count()["survived"].index, df.groupby("pclass").count()["survived"])
# plt.show()

# 散布図
plt.scatter(df["fare"], df["age"], alpha=0.2)
plt.show()