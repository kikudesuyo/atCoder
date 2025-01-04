n = int(input())


grid = [[""] * n for _ in range(n)]
grid[(n + 1) // 2 - 1][(n + 1) // 2 - 1] = "T"

num = 1
r, c = (0, 0)
vectors = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
v_i = 0

while num < n**2:
    grid[r][c] = num
    if (
        r + vectors[v_i][0] < 0
        or r + vectors[v_i][0] >= n
        or c + vectors[v_i][1] < 0
        or c + vectors[v_i][1] >= n
        or grid[r + vectors[v_i][0]][c + vectors[v_i][1]] not in ["", "T"]
    ):
        v_i = (v_i + 1) % 4
        continue
    r += vectors[v_i][0]
    c += vectors[v_i][1]
    num += 1


for row in grid:
    print(" ".join(map(str, row)))
