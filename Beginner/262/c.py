n = int(input())

a_n = list(map(int, input().split()))

same_idx_cnt = 0
diff_arr = []
for i in range(n):
    if i + 1 == a_n[i]:
        same_idx_cnt += 1
    else:
        t = (i + 1, a_n[i])
        diff_arr.append((min(t), max(t)))

diff_cnt = len(diff_arr) - len(set(diff_arr))

print(same_idx_cnt * (same_idx_cnt - 1) // 2 + diff_cnt)
