h, w = map(int, input().split())
s_h = [input() for _ in range(h)]


min_r, max_r, min_c, max_c = h - 1, 0, w - 1, 0


for row in range(h):
    for col in range(w):
        if s_h[row][col] == "#":
            if row < min_r:
                min_r = row
            if row > max_r:
                max_r = row
            if col < min_c:
                min_c = col
            if col > max_c:
                max_c = col


recs = [[0] * (max_c - min_c + 1) for _ in range(max_r - min_r + 1)]

for row in range(min_r, max_r + 1):
    for col in range(min_c, max_c + 1):
        if s_h[row][col] == ".":
            print("No")
            exit()

print("Yes")
