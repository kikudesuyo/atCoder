a, b = map(int, input().split())

diff = a - b

if diff == 0:
    print(1)
elif diff % 2 == 0:
    print(3)
else:
    print(2)
