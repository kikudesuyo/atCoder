s = list(input())
cnt = 0
i = 0
while i < len(s):
    if s[i : i + 2] == ["0", "0"]:
        cnt += 1
        i += 2
    else:
        i += 1
print(len(s) - cnt)
