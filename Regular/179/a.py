n, k = map(int, input().split())
a_s = list(map(int, input().split()))

total = sum(a_s)

if k > 0:
    print("Yes")
    print(*sorted(a_s))
    exit()

if total < k:
    print("No")

else:
    print("Yes")
    sorted_a_s = sorted(a_s, reverse=True)
    print(*sorted_a_s)
