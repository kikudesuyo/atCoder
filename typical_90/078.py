n, m = map(int, input().split())

ab_s = [list(map(int, input().split())) for _ in range(m)]

vertex_dict = {}
for i in range(1, n + 1):
    vertex_dict[i] = []
for a, b in ab_s:
    if a > b:
        vertex_dict[a].append(b)
    elif a < b:
        vertex_dict[b].append(a)


count = 0
for elem in vertex_dict.values():
    if len(elem) == 1:
        count += 1
print(count)
