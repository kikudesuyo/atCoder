n, a, b = map(int, input().split())


white_tiles = [["." for _ in range(b)] for _ in range(a)]
black_tiles = [["#" for _ in range(b)] for _ in range(a)]


is_white = True
ans = []
for i in range(n):
    if is_white:
        rows = []
        for i in range(a):
            tmp_rows = []
            for j in range(n):
                if j % 2 == 0:
                    tmp_rows.append("".join(white_tiles[i]))
                else:
                    tmp_rows.append("".join(black_tiles[i]))

            rows.append("".join(tmp_rows))
    else:
        rows = []
        for i in range(a):
            tmp_rows = []
            for j in range(n):
                if j % 2 == 0:
                    tmp_rows.append("".join(black_tiles[i]))
                else:
                    tmp_rows.append("".join(white_tiles[i]))

            rows.append("".join(tmp_rows))
    ans.append(rows)
    is_white = not is_white


for rows in ans:
    for row in rows:
        print(row)
