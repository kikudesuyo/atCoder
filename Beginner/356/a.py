n, l, r = map(int, input().split())

left_arr = []
for i in range(1, l):
    left_arr.append(i)
middle_arr = []
for i in range(l, r + 1):
    middle_arr.append(i)
middle_arr.reverse()
right_arr = []
for i in range(r + 1, n + 1):
    right_arr.append(i)

print(" ".join(list(map(str, left_arr + middle_arr + right_arr))))
