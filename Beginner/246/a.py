x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

if [x1, x2, x3].count(x1) == 1:
    x = x1
if [x1, x2, x3].count(x2) == 1:
    x = x2
if [x1, x2, x3].count(x3) == 1:
    x = x3


if [y1, y2, y3].count(y1) == 1:
    y = y1
if [y1, y2, y3].count(y2) == 1:
    y = y2
if [y1, y2, y3].count(y3) == 1:
    y = y3

print(x, y)
