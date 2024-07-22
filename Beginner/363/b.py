n, t, p = map(int, input().split())
l_s = list(map(int, input().split()))


for i in range(t):
    p_count = 0
    for j in range(n):
        if l_s[j] >= t:
            p_count += 1
    if p_count >= p:
        print(i)
        exit()
    p_count = 0
    l_s = list(map(lambda x: x + 1, l_s))
