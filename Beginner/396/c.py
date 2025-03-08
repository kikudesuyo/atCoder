n, m = map(int, input().split())
b_n = list(map(int, input().split()))
w_m = list(map(int, input().split()))

s_b = sorted(b_n, reverse=True)
s_w = sorted(w_m, reverse=True)

cnt = 0
i = 0
while i < n and i < m:
    if s_b[i] + s_w[i] < 0:
        break
    if s_w[i] < 0:
        while i < n and s_b[i] >= 0:
            cnt += s_b[i]
            i += 1
            if i == n:
                print(cnt)
                exit()
        print(cnt)
        exit()
    cnt += s_b[i] + s_w[i]
    i += 1


while i < n:
    if s_b[i] < 0:
        print(cnt)
        exit()
    cnt += s_b[i]
    i += 1


print(cnt)
