n = int(input())
s_s = [input() for _ in range(n)]


counts = {}
for i in range(n):
    if not s_s[i].count("o") in counts:
        counts[s_s[i].count("o")] = [i + 1]
    else:
        counts[s_s[i].count("o")].append(i + 1)

ranks = []
for i in reversed(range(n)):
    if not i in counts:
        continue
    ranks.extend(counts[i])
print(*ranks)
