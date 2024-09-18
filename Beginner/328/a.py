n, x = map(int, input().split())
s_s = list(map(int, input().split()))

count = 0
for i in s_s:
    if i <= x:
        count += i

print(count)
