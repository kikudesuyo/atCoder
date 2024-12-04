n, x = map(int, input().split())
ab_n = [list(map(int, input().split())) for _ in range(n)]

a, b = ab_n[0]
idxes = [a, b]
for i in range(1, n):
    a, b = ab_n[i]
    past_idxes = idxes.copy()
    idxes = []
    for elem in past_idxes:
        idxes.append(a + elem)
        idxes.append(b + elem)
    idxes = list(set(idxes))
    idexes = [elem for elem in idxes if elem <= x]


if x in idxes:
    print("Yes")
else:
    print("No")
