### pop, appendを用いた方法だとO(n*k)となりTLEになる
# n, k = list(map(int, input().split()))
# p_s = list(map(int, input().split()))

# dict = {}
# for i in range(len(p_s)):
#     dict[p_s[i]] = i + 1
# diffs = []
# good_array = []
# for i in range(1, len(p_s) + 2 - k):
#     if i == 1:
#         for j in range(1, k + 1):
#             good_array.append(dict[j])
#     else:
#         good_array.pop(0)
#         good_array.append(dict[i + k - 1])
#     diff = max(good_array) - min(good_array)
#     diffs.append(diff)
# print(min(diffs))

### アルゴリズムは同じ、SortedSetを使用することでO(NlogK)となりACになる
from sortedcontainers import SortedSet

n, k = map(int, input().split())
p = list(map(int, input().split()))
idxes = [None for _ in range(n)]
for n in range(n):
    idxes[p[n] - 1] = n + 1

good_array = SortedSet()
for n in range(k):
    good_array.add(idxes[n])
min = good_array[k - 1] - good_array[0]
for n in range(1, n - k + 1):
    good_array.discard(idxes[n - 1])
    good_array.add(idxes[n + k - 1])
    if min is None or good_array[k - 1] - good_array[0] < min:
        min = good_array[k - 1] - good_array[0]
print(min)
