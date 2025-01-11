n = int(input())
a_n = list(map(int, input().split()))

if n % 2 == 0:
    top_mochies = a_n[: n // 2]
    base_mochies = a_n[n // 2 :]
else:
    top_mochies = a_n[: n // 2]
    base_mochies = a_n[n // 2 + 1 :]


top_idx = 0
base_idx = 0
cnt = 0
while top_idx < len(top_mochies) and base_idx < len(base_mochies):
    if top_mochies[top_idx] * 2 <= base_mochies[base_idx]:
        cnt += 1
        top_idx += 1
        base_idx += 1
    else:
        base_idx += 1

print(cnt)
