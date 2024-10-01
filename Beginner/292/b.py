n, q = map(int, input().split())
events = [list(map(int, input().split())) for _ in range(q)]
cards = [0] * n
for event in events:
    c, x = event
    if c == 1:
        cards[x - 1] += 1
    elif c == 2:
        cards[x - 1] += 2
    else:
        if cards[x - 1] >= 2:
            print("Yes")
        else:
            print("No")
