n, k = map(int, input().split())
a_n = list(map(int, input().split()))

for i in range(k):
    a_n.pop(0)
    a_n.append(0)

print(*a_n)
