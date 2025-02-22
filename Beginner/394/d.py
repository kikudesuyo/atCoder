s = list(input())


if len(s) % 2 != 0:
    print("No")
    exit()


j = {")": "(", "]": "[", "}": "{"}
stack = []


for i in range(len(s)):
    if s[i] in j.values():
        stack.append(s[i])
    elif s[i] in j.keys():
        if len(stack) == 0:
            print("No")
            exit()
        if stack[-1] == j[s[i]]:
            stack.pop()
        else:
            print("No")
            exit()

print("Yes")
