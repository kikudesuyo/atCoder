n = int(input())
x_total, y_total = 0, 0
for i in range(n):
    x, y = map(int, input().split())
    x_total += x
    y_total += y

if x_total > y_total:
    print("Takahashi")
elif x_total < y_total:
    print("Aoki")
else:
    print("Draw")
