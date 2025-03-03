n = int(input())

grids = [["." for _ in range(n)] for _ in range(n)]

for i in range(1, n + 1):
    j = n + 1 - i
    if i > j:
        continue
    if i % 2 == 1:
        for r in range(i - 1, j):
            for c in range(i - 1, j):
                grids[r][c] = "#"
    else:
        for r in range(i - 1, j):
            for c in range(i - 1, j):
                grids[r][c] = "."


for i in range(n):
    print("".join(grids[i]))
