s, t, x = map(int, input().split())

if s < t:
    if s <= x < t:
        print("Yes")
    else:
        print("No")
else:
    if t <= x < s:
        print("No")
    else:
        print("Yes")
