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

###アルゴリズムは同じ、SortedSetを使用することでオーダーがlogNとなりACになる
N, K = map(int, input().split())
P = list(map(int, input().split()))
R = [None for _ in range(N)]
for n in range(N):
    R[P[n] - 1] = n + 1
from sortedcontainers import SortedSet

SS = SortedSet()
for n in range(K):
    SS.add(R[n])
min = SS[K - 1] - SS[0]
for n in range(1, N - K + 1):
    SS.discard(R[n - 1])
    SS.add(R[n + K - 1])
    if min is None or SS[K - 1] - SS[0] < min:
        min = SS[K - 1] - SS[0]
print(min)
