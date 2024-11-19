n, k = map(int, input().split())
s = list(input())
cnt = 0
t = 0
for i in range(len(s)):
    if s[i] == "O":
        t += 1
    else:
        t = 0
    if t % k == 0:
        cnt += 1
print(cnt)
