r, g, b = map(int, input().split())
c = input()

if c == "Red":
    if g > b:
        print(b)
    else:
        print(g)
elif c == "Green":
    if r > b:
        print(b)
    else:
        print(r)
else:
    if r > g:
        print(g)
    else:
        print(r)
