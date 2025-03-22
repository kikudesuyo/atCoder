n, r, c = map(int, input().split())
s = list(input())

smokes = set()

smokes.add((0, 0))

target = (r, c)
current = (0, 0)
ans = []
for i in range(n):
    if s[i] == "N":
        target = (target[0] + 1, target[1])
        current = (current[0] + 1, current[1])
        smokes.add(current)
    elif s[i] == "W":
        target = (target[0], target[1] + 1)
        current = (current[0], current[1] + 1)
        smokes.add(current)
    elif s[i] == "S":
        target = (target[0] - 1, target[1])
        current = (current[0] - 1, current[1])
        smokes.add(current)
    elif s[i] == "E":
        target = (target[0], target[1] - 1)
        current = (current[0], current[1] - 1)
        smokes.add(current)
    if target in smokes:
        ans.append(1)
    else:
        ans.append(0)

print("".join(map(str, ans)))
