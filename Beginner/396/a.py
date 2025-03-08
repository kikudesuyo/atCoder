n = int(input())
a_n = list(map(int, input().split()))


for i in range(n - 2):
    a, b, c = a_n[i], a_n[i + 1], a_n[i + 2]
    if a == b and b == c:
        print("Yes")
        exit()

print("No")
