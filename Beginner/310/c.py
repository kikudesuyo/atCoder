n = int(input())
s_n = [input() for _ in range(n)]

set_s = list(set(s_n))

young_s = []
for i in range(len(set_s)):
    if set_s[i] > set_s[i][::-1]:
        young_s.append(set_s[i][::-1])
    else:
        young_s.append(set_s[i])

set_young_s = set(young_s)
print(len(set_young_s))
