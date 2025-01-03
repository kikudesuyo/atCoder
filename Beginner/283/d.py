s = ["("] + list(input()) + [")"]


stack = []
used = set()
for i in range(len(s)):
    if s[i] == "(":
        stack.append([])
    elif s[i] == ")":
        for c in stack[-1]:
            if c not in used:
                print("No")
                exit()
            used.remove(c)
        stack.pop()

    else:
        stack[-1].append(s[i])
        used.add(s[i])

for c in stack:
    for cc in c:
        if used.discard(cc) == None:
            print("No")
            exit()

print("Yes")
