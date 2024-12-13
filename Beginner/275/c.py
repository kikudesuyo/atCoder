from itertools import combinations

s_n = [list(input()) for _ in range(9)]

pawns = set()
for i in range(9):
    for j in range(9):
        if s_n[i][j] == "#":
            pawns.add((i, j))

if len(pawns) == 0:
    print(0)
    exit()

arr = []
for i in range(9):
    for j in range(9):
        arr.append((i, j))


def is_square(a, b, c, d):
    ab = (b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2
    ac = (c[0] - a[0]) ** 2 + (c[1] - a[1]) ** 2
    ad = (d[0] - a[0]) ** 2 + (d[1] - a[1]) ** 2
    bc = (c[0] - b[0]) ** 2 + (c[1] - b[1]) ** 2
    bd = (d[0] - b[0]) ** 2 + (d[1] - b[1]) ** 2
    cd = (d[0] - c[0]) ** 2 + (d[1] - c[1]) ** 2
    distances = [ab, ac, ad, bc, bd, cd]
    min_num = min(distances)
    max_num = max(distances)
    if distances.count(min_num) == 4 and distances.count(max_num) == 2:
        return True
    else:
        return False


c = combinations(arr, 4)
ans = []
for points in c:
    p_a, p_b, p_c, p_d = points
    if p_a in pawns and p_b in pawns and p_c in pawns and p_d in pawns:
        if is_square(p_a, p_b, p_c, p_d):
            ans.append(points)

print(len(ans))
