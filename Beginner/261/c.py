n = int(input())
s_arr = [input() for _ in range(n)]

set_s = set(s_arr)

dict = {}
for s in set_s:
    dict[s] = 0

for string in s_arr:
    if dict[string] == 0:
        print(string)
    else:
        print(string + f"({dict[string]})")
    dict[string] += 1
