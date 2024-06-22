n = int(input())
a_s = list(map(int, input().split()))
count = 0
for i in range(len(a_s)):
    if i == len(a_s) - 2:
        break
    if a_s[i] == a_s[i + 2]:
        count += 1

print(count)
