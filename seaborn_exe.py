# Seaborn:

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

df = sns.load_dataset("titanic")

# sns.displot(df["age"])
# plt.show()

# sns.countplot(x="pclass", data=df)
# sns.catplot(x="pclass", data=df, kind="count")
# plt.show()

# sns.barplot(x="survived", y="age", hue="sex", data=df)
# plt.show()

# 箱ひげ図
# sns.boxplot(x="survived", y="age", hue="sex", data=df)
# plt.show()

# バイオリンプロット
# sns.violinplot(x="survived", y="age", hue="sex", data=df)
# plt.show()

# sns.jointplot(x="age", y="fare", data=df)
# plt.show()

# sns.pairplot(df[["age", "fare"]])
# plt.show()

df = sns.load_dataset("iris")
sns.pairplot(df)
plt.show()
