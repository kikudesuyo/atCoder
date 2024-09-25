s = input()

idx = -1
for i in range(len(s)):
    if s[i] == "a":
        idx = i + 1

print(idx)
