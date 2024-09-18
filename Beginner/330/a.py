n, l = map(int, input().split())
a_n = list(map(int, input().split()))

count = 0
for i in a_n:
    if i >= l:
        count += 1

print(count)
