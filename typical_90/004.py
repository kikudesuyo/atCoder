h, w = map(int, input().split())

a_matrix = [list(map(int, input().split())) for _ in range(h)]

tranposition_a_matrix = [[a_matrix[j][i] for j in range(h)] for i in range(w)]


b_matrix = [[0 for _ in range(w)] for _ in range(h)]

col_sums = []
for j in range(w):
    col_sums.append(sum(tranposition_a_matrix[j]))

row_sums = []
for i in range(h):
    row_sums.append(sum(a_matrix[i]))


for i in range(h):
    for j in range(w):
        b_matrix[i][j] = row_sums[i] + col_sums[j] - a_matrix[i][j]


for i in range(h):
    print(*b_matrix[i])
