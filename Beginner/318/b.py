n = int(input())
abcd_n = [list(map(int, input().split())) for _ in range(n)]


area = [[False for _ in range(101)] for _ in range(101)]
for i in range(n):
    a, b, c, d = abcd_n[i]
    for j in range(a + 1, b + 1):
        for k in range(c + 1, d + 1):
            area[j][k] = True

print(sum([sum(a) for a in area]))
