n = int(input())
a_n = list(map(int, input().split()))

base_mothi_idx = 0

cnt = 0
for top_idx in range(n):
    top_mothi = a_n[top_idx]
    while top_mothi * 2 > a_n[base_mothi_idx] and base_mothi_idx < n - 1:
        base_mothi_idx += 1
    if top_mothi * 2 <= a_n[base_mothi_idx]:
        cnt += n - base_mothi_idx

print(cnt)
