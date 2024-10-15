from itertools import combinations as combi

n, m = map(int, input().split())
uv_m = [list(map(int, input().split())) for _ in range(m)]


dict = {}
for uv in uv_m:
    u, v = uv
    if not u in dict.keys():
        if u < v:
            dict[u] = [v]
    else:
        if u < v:
            dict[u].append(v)
    if not v in dict.keys():
        if v < u:
            dict[v] = [u]
    else:
        if v < u:
            dict[v].append(u)


temp = []
for key in dict.keys():
    values = dict[key]
    if len(values) < 2:
        continue
    combinations = combi(values, 2)
    for combination in combinations:
        combination = list(combination)
        if min(combination) in dict.keys():
            if max(combination) in dict[min(combination)]:
                temp.append([key, min(combination), max(combination)])

print(len(temp))
