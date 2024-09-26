a, b = map(int, input().split())

rate = str(round(b / a, 3))

if len(rate) != 5:
    print(rate + "00")
else:
    print(rate)
