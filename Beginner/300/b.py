h, w = map(int, input().split())
a_hw = [list(input()) for _ in range(h)]
b_hw = [tuple(input()) for _ in range(h)]


for i in range(h):
    row_shift_a = a_hw[i:] + a_hw[:i]
    for j in range(w):
        matrix_a = list(zip(*row_shift_a))
        col_matrix_a = matrix_a[j:] + matrix_a[:j]
        col_shift_a = list(zip(*col_matrix_a))
        if col_shift_a == b_hw:
            print("Yes")
            exit()

print("No")
