n = int(input())
s_n = [input() for _ in range(n)]

s_d = []
for i in range(n):
    s_d.append((s_n[i], len(s_n[i])))


sorted_s = sorted(s_d, key=lambda x: (x[1], x[0]))

ans = []
for i in range(n):
    ans.append(sorted_s[i][0])

print("".join(ans))
