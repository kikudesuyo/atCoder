n, p = map(int, input().split())
a_n = list(map(int, input().split()))

count = 0
for a in a_n:
    if a < p:
        count += 1

print(count)
