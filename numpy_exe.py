# Numpy: 大量演算, ベクトル演算・行列演算が得意

import numpy as np

# 配列: ベクトル演算がされる
a = np.array([1, 2, 3])
b = np.array([10, 20, 30])
print(a + b)
print(a*2)

# リスト: 
aa = [1,2,3]
bb = [10,20,30]
print(aa + bb)
print(aa*2)

# 統計量計算
aaa = np.array([1,2,3,4,5])
np.sum(aaa)
np.mean(aaa)
np.median(aaa)
np.std(aaa) # 標準偏差

# 多次元配列
A = np.array([[1, 2], [3, 4], [5, 6]])
print(A.shape)
A.T # 転置
print(A.T.shape)

scores = np.array([80, 90, 75, 100])
mean = np.mean(scores)
print(scores - mean)

random = np.random.rand(3, 2)
print(random)
zeros = np.zeros([3, 2])
print(zeros)
arange = np.arange(0, 10, 2)
print(arange)
