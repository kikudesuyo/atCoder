n, q = map(int, input().split())
x_q = [int(input()) for _ in range(q)]


d = {}  # key: ball_val, value: index
for i in range(n):
    d[i + 1] = i

arr = [i + 1 for i in range(n)]  # ball nums


for x in x_q:
    if d[x] == n - 1:
        l_idx, r_idx = d[x] - 1, d[x]
        left_val, right_val = arr[l_idx], arr[r_idx]

        arr[l_idx], arr[r_idx] = arr[r_idx], arr[l_idx]
        d[left_val], d[right_val] = r_idx, l_idx

    else:
        l_idx, r_idx = d[x], d[x] + 1
        left_val, right_val = arr[l_idx], arr[r_idx]

        arr[l_idx], arr[r_idx] = arr[r_idx], arr[l_idx]
        d[left_val], d[right_val] = r_idx, l_idx

print(*arr)
