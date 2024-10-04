import math

a, b, d = map(int, input().split())
theta = math.atan2(b, a) + math.radians(d)
distance = math.sqrt(a**2 + b**2)

c, d = distance * math.cos(theta), distance * math.sin(theta)

print(c, d)
