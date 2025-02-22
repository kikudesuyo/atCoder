s = list(input())

cnt = 0
for i in range(len(s)):
    for j in range(i, len(s)):
        _ = None
        if s[i] == "A" and s[j] == "B" and j + j - i < len(s) and s[j + j - i] == "C":
            cnt += 1

print(cnt)
