n, m = list(map(int, input().split()))
a_m = list(map(int, input().split()))

temp_arr = []
for i in range(n):
    temp_arr.append(i + 1)
if 1 in a_m or n in a_m:
    print(-1)
    exit()

sorted_a_m = sorted(a_m)
for a_i in sorted_a_m:
    temp_arr[a_i - 1], temp_arr[a_i] = temp_arr[a_i], temp_arr[a_i - 1]

str_arr = list(map(str, temp_arr))
print(" ".join(str_arr))
