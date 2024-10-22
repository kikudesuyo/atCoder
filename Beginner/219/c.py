x = input()
n = int(input())
s_n = [input() for _ in range(n)]

s_dict = {}
for i in range(26):
    s_dict[x[i]] = i + 1
sorted_arr = sorted(s_n, key=lambda x: [s_dict[s] for s in x])

for s in sorted_arr:
    print(s)
