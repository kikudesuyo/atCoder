import math

a, b = map(int, input().split())

distance = math.sqrt(a**2 + b**2)

print(a / distance, b / distance)
