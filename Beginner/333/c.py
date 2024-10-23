n = int(input())

sum_arr = []
for i in range(1, 100):
    first = int("1" * i)
    for j in range(i, 100):
        second = int("1" * j)
        for k in range(1, 100):
            third = int("1" * k)
            sum_arr.append(first + second + third)

sorted_sum = sorted(set(sum_arr))

print(sorted_sum[n - 1])
