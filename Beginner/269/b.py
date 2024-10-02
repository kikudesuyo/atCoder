s_n = [input() for _ in range(10)]


min_i, min_j, max_i, max_j = 11, 11, -1, -1
for i in range(10):
    for j in range(10):
        if s_n[i][j] == "#":
            min_i = min(min_i, i)
            min_j = min(min_j, j)
            max_i = max(max_i, i)
            max_j = max(max_j, j)

print(min_i + 1, max_i + 1)
print(min_j + 1, max_j + 1)
