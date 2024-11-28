# 俯角とは見下ろす角度

import math

t = int(input())
l, x, y = map(int, input().split())
q = int(input())
e_q = [int(input()) for _ in range(q)]

for e in e_q:
    current = e % t
    current_shita = -(2 * math.pi * current / t) + (3 * math.pi / 2)
    w_y = (l / 2) * math.cos(current_shita)
    w_z = l / 2 + (l / 2) * math.sin(current_shita)
    shita = math.atan(w_z / math.sqrt(x**2 + (y - w_y) ** 2))
    print(math.degrees(shita))
