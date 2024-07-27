h, w = map(int, input().split())
s_i, s_j = map(int, input().split())
s_i -= 1
s_j -= 1

array = []
for i in range(h):
    c_s = input()
    array.append(c_s)

string = input()

for str in string:
    if str == "L":
        if s_j - 1 < 0:
            continue
        if array[s_i][s_j - 1] == ".":
            s_j -= 1
    if str == "R":
        if s_j >= w - 1:
            continue
        if array[s_i][s_j + 1] == ".":
            s_j += 1
    if str == "U":
        if s_i - 1 < 0:
            continue
        if array[s_i - 1][s_j] == ".":
            s_i -= 1
    if str == "D":
        if s_i >= h - 1:
            continue
        if array[s_i + 1][s_j] == ".":
            s_i += 1

print(s_i + 1, s_j + 1)
