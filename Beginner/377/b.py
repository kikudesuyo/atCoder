s_n = [list(input()) for _ in range(8)]


rows = []
cols = []
for r in range(len(s_n)):
    for c in range(len(s_n)):
        if s_n[r][c] == "#":
            rows.append(r)
            cols.append(c)
left_r = 8 - len(set(rows))
left_c = 8 - len(set(cols))

print(left_r * left_c)
