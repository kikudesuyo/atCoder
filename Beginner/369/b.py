n = int(input())

count = 0
l_idx = -1
r_idx = -1
for i in range(n):
    str_a, s = input().split()
    int_a = int(str_a)
    if s == "L":
        if l_idx == -1:
            l_idx = int_a
        else:
            count += abs(l_idx - int_a)
            l_idx = int_a
    else:
        if r_idx == -1:
            r_idx = int_a
        else:
            count += abs(r_idx - int_a)
            r_idx = int_a
print(count)
