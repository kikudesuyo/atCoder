n = int(input())
a_n = list(map(int, input().split()))

if n % 2 == 0:
    top_mothies = a_n[: n // 2]
    base_mothies = a_n[n // 2 :]
else:
    top_mothies = a_n[: n // 2]
    base_mothies = a_n[n // 2 + 1 :]


top_idx = 0
base_idx = 0
cnt = 0
while top_idx < len(top_mothies) and base_idx < len(base_mothies):
    if top_mothies[top_idx] * 2 <= base_mothies[base_idx]:
        cnt += 1
        top_idx += 1
        base_idx += 1
    else:
        base_idx += 1

print(cnt)
