n, x = map(int, input().split())
a_n = list(map(int, input().split()))

sorted_a_n = sorted(a_n)
right_idx = 1
for left_idx in range(n):
    while abs(sorted_a_n[right_idx] - sorted_a_n[left_idx]) < abs(x):
        if right_idx == n - 1:
            break
        else:
            right_idx += 1
    diff = abs(sorted_a_n[right_idx] - sorted_a_n[left_idx])
    if diff == abs(x):
        print("Yes")
        exit()

print("No")
