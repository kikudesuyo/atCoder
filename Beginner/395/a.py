n = int(input())
a_n = list(map(int, input().split()))

if len(set(a_n)) != n:
    print("No")
    exit()

s_an = sorted(a_n)

if s_an == a_n:
    print("Yes")
else:
    print("No")
