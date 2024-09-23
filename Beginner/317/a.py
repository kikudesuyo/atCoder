n, h, x = map(int, input().split())
p_s = list(map(int, input().split()))
answer = n
for i in range(len(p_s)):
    if x <= h + p_s[i]:
        answer = min(answer, i + 1)
print(answer)
