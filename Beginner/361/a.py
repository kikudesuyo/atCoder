n, k, x = map(int, input().split())
a_n = list(map(int, input().split()))
a_n.insert(k, x)
print(*a_n)
