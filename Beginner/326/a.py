x, y = map(int, input().split())

diff = y - x
if -3 <= diff <= 2:
    print("Yes")
else:
    print("No")
