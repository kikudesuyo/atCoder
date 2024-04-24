n, a, b = list(map(int, input().split()))
d_i = list(map(int, input().split()))

week_days = a + b

remainder = [plan % week_days for plan in d_i]
min, max = min(remainder), max(remainder)
if max - min < a:
    print("Yes")
else:
    print("No")
