n = int(input())
a_n = list(map(int, input().split()))

base_mochi_idx = 0

cnt = 0
for top_idx in range(n):
    top_mochi = a_n[top_idx]
    while top_mochi * 2 > a_n[base_mochi_idx] and base_mochi_idx < n - 1:
        base_mochi_idx += 1
    if top_mochi * 2 <= a_n[base_mochi_idx]:
        cnt += n - base_mochi_idx

print(cnt)
