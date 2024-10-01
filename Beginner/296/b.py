s_n = [input() for _ in range(8)]

cols = "abcdefgh"
rows = "87654321"

x, y = 100, 100
for i in range(len(s_n)):
    if "*" in s_n[i]:
        x = rows[i]
        y = cols[s_n[i].index("*")]
print(y + x)
