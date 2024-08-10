n, t, a = map(int, input().split())

left = n - (t + a)

if t >= a:
    if left + a >= t:
        print("No")
        exit()
else:
    if left + t >= a:
        print("No")
        exit()

print("Yes")
