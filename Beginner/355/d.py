import math

n = int(input())
min_to_idx = {}
idx_to_max = {}
for idx in range(n):
    l, r = list(map(int, input().split()))
    min_to_idx[l] = idx
    idx_to_max[idx] = r

min_sorted = sorted(min_to_idx.keys())


count = 0
max_r = 0
idx_list = []
for i in range(n):
    if i == 0:
        min_l = min_sorted[i]
        max_r = idx_to_max[min_to_idx[min_l]]
        continue
    if max_r <= min_sorted[i]:
        count += math.comb(len(idx_list) + 1, 2)
        min_l = min_sorted[i]
        max_r = min(idx_list)
        idx_list = []
    # 範囲を含まないときは、maxの値を更新
    else:
        idx_list.append(idx_to_max[min_to_idx[min_sorted[i]]])


print(count)
