a = list(map(int, input().split()))

sorted_a = sorted(a)

if sorted_a[0] * sorted_a[1] == sorted_a[2]:
    print("Yes")

else:
    print("No")
