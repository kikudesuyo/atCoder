x_a, y_a = map(int, input().split())
x_b, y_b = map(int, input().split())
x_c, y_c = map(int, input().split())
import math

ab = math.sqrt((x_a - x_b) ** 2 + (y_a - y_b) ** 2)
bc = math.sqrt((x_b - x_c) ** 2 + (y_b - y_c) ** 2)
ca = math.sqrt((x_c - x_a) ** 2 + (y_c - y_a) ** 2)

if ab > bc and ab > ca:
    if math.isclose(bc**2 + ca**2, ab**2, rel_tol=1e-9):
        print("Yes")
        exit()
if bc > ab and bc > ca:
    if math.isclose(ab**2 + ca**2, bc**2, rel_tol=1e-9):
        print("Yes")
        exit()

if ca > ab and ca > bc:
    if math.isclose(ab**2 + bc**2, ca**2, rel_tol=1e-9):
        print("Yes")
        exit()

print("No")
