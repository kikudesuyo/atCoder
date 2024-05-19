n, a, b = list(map(int, input().split()))
d = list(map(int, input().split()))

week_days = a + b

remainder = [plan % week_days for plan in d]

set = list(map(int, set(remainder)))

sort = sorted(set)
diff = 0
# for i in range(len(sort)):
#     if i == len(sort) - 1:
#         break
#     if sort[i + 1] - sort[i] > diff:
#         diff = sort[i + 1] - sort[i]
for i in range(len(sort)):
    j = (i + len(sort) - 1) % len(sort)
    length = (sort[j] - sort[i]) % week_days + 1
    diff = min(diff, length)
if diff <= a:
    print("Yes")
else:
    print("No")
