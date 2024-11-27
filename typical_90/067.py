import numpy as np

str_n, str_k = input().split()
k = int(str_k)


for i in range(k):
    str_n = np.base_repr(int(str_n, 8), 9)
    str_n = str_n.replace("8", "5")

print(str_n)
