n, m = map(int, input().split())
s_n = [input() for _ in range(n)]
count = 0
next = False
for i in range(len(s_n)):
    for j in range(len(s_n)):
        if i <= j:
            continue
        first = s_n[i]
        second = s_n[j]
        for k in range(m):
            if not (first[k] == "o" or second[k] == "o"):
                next = True
                break
        if next:
            next = False
        else:
            count += 1
print(count)
