n, x = map(int, input().split())
a_n = list(map(int, input().split()))


is_known = [False] * n


idx = x - 1
for i in range(n):
    if is_known[idx]:
        break
    is_known[idx] = True
    idx = a_n[idx] - 1
print(is_known.count(True))
