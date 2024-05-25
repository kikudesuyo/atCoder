n, t = list(map(int, input().split()))
a_s = list(map(int, input().split()))

idx_to_row = {}
idx_to_column = {}
for i in range(n):
    idx_to_row[i] = 0
    idx_to_column[i] = 0
diagonal_1 = 0
diagonal_2 = 0

count = 1
for i in range(len(a_s)):
    coodinate = a_s[i] - 1
    x, y = coodinate // n, coodinate % n
    row_num = idx_to_row[x] + 1
    idx_to_row[x] = row_num
    colum_num = idx_to_column[y] + 1
    idx_to_column[y] = colum_num
    if x == y:
        diagonal_1 += 1
    if x + y == n - 1:
        diagonal_2 += 1
    if row_num == n or colum_num == n or diagonal_1 == n or diagonal_2 == n:
        print(count)
        exit()
    count += 1
print(-1)
