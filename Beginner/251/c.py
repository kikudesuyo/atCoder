n = int(input())
st_n = [list(map(str, input().split())) for _ in range(n)]

set_s = set()

max_num = 0
idx = 0
for i, st in enumerate(st_n):
    s, t = st[0], int(st[1])
    if s in set_s:
        continue
    else:
        set_s.add(s)
        if max_num < t:
            idx = i
            max_num = t

print(idx + 1)
