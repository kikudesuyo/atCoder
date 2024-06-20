h, w, n = map(int, input().split())
t = input()
s_s = [input() for _ in range(h)]

count = 0

for i in range(h):
    for j in range(w):
        if s_s[i][j] == "#":
            continue
        row, column = i, j
        for idx, command in enumerate(t):
            if row < 0 or column < 0 or row >= h or column >= w:
                break
            if command == "L":
                column -= 1
            if command == "R":
                column += 1
            if command == "U":
                row -= 1
            if command == "D":
                row += 1
            if s_s[row][column] == "#":
                break
            if idx == len(t) - 1:
                count += 1
print(count)
