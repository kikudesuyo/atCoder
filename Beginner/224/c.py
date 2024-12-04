from itertools import combinations

n = int(input())
xy_n = [list(map(int, input().split())) for _ in range(n)]


c = list(combinations(range(n), 3))


def is_line(p1, p2, p3):
    if p2[0] - p1[0] == 0 or p3[0] - p2[0] == 0:
        if p2[0] - p1[0] == 0 and p3[0] - p2[0] == 0:
            return True
        return False
    a1 = (p2[1] - p1[1]) / (p2[0] - p1[0])
    a2 = (p3[1] - p2[1]) / (p3[0] - p2[0])
    return a1 == a2


cnt = 0
for i in c:
    a, b, c = i
    p1, p2, p3 = xy_n[a], xy_n[b], xy_n[c]
    if not is_line(p1, p2, p3):
        cnt += 1
print(cnt)
