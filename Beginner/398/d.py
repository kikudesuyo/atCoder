n, r, c = map(int, input().split())
s = list(input())

smokes = set()
smokes.add((0, 0))
takahashi = (r, c)
smoke_source = (0, 0)
ans = []
for i in range(n):
    if s[i] == "N":
        takahashi = (takahashi[0] + 1, takahashi[1])
        smoke_source = (smoke_source[0] + 1, smoke_source[1])
    elif s[i] == "W":
        takahashi = (takahashi[0], takahashi[1] + 1)
        smoke_source = (smoke_source[0], smoke_source[1] + 1)
    elif s[i] == "S":
        takahashi = (takahashi[0] - 1, takahashi[1])
        smoke_source = (smoke_source[0] - 1, smoke_source[1])
    elif s[i] == "E":
        takahashi = (takahashi[0], takahashi[1] - 1)
        smoke_source = (smoke_source[0], smoke_source[1] - 1)
    smokes.add(smoke_source)
    if takahashi in smokes:
        ans.append(1)
    else:
        ans.append(0)

print("".join(map(str, ans)))
