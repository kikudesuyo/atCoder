s = input()
idx = 0
for i in range(len(s)):
    if s[i] == ".":
        idx = i
print(s[idx + 1 :])
