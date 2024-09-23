n = int(input())
a_s = list(map(int, input().split()))
count = 0
arr = []
for i in range(len(a_s)):
    count += a_s[i]
    if (i + 1) % 7 == 0:
        arr.append(count)
        count = 0
print(*arr)
