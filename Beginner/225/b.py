n = int(input())
ab_list = [list(map(int, input().split())) for _ in range(n - 1)]
dict = {}
for ab in ab_list:
    a, b = ab
    if a not in dict:
        dict[a] = [b]
    else:
        dict[a].append(b)
    if b not in dict:
        dict[b] = [a]
    else:
        dict[b].append(a)
for value in dict.values():
    if len(list(set(value))) == n - 1:
        print("Yes")
        exit()
print("No")
