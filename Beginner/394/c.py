s = list(input())

for i in reversed(range(len(s))):
    if s[i : i + 2] == ["W", "A"]:
        s[i : i + 2] = ["A", "C"]

print("".join(s))
