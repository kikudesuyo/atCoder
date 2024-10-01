n, m = map(int, input().split())
ab_m = [list(map(int, input().split())) for _ in range(m)]
dict = {}
for a, b in ab_m:
    if a in dict:
        dict[a].append(b)
    else:
        dict[a] = [b]
    if b in dict:
        dict[b].append(a)
    else:
        dict[b] = [a]
for key in range(1, n + 1):
    if key not in dict.keys():
        print(0)
        continue
    result = [len(dict[key])] + sorted(dict[key])
    print(*result)
