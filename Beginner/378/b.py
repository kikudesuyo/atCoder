n = int(input())
qr_n = [list(map(int, input().split())) for _ in range(n)]
q = int(input())
td_q = [list(map(int, input().split())) for _ in range(q)]

for td in td_q:
    t, d = td
    q, r = qr_n[t - 1]
    if (d - r) % q == 0:
        print(d)
    else:
        raw_div = (d - r) // q
        print(r + (raw_div + 1) * q)
