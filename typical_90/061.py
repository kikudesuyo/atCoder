q = int(input())
tx_s = [list(map(int, input().split())) for _ in range(q)]


first_half = []
second_half = []
for t, x in tx_s:
    if t == 1:
        first_half.append(x)
    elif t == 2:
        second_half.append(x)
    else:
        if len(first_half) >= x:
            print(first_half[-x])
        else:
            print(second_half[x - len(first_half) - 1])
