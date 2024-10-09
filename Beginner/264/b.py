r, c = map(int, input().split())
chebyshev_distance = max(abs(r - 8), abs(c - 8))
if chebyshev_distance % 2 == 0:
    print("white")
else:
    print("black")
