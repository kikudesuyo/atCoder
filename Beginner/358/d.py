n, m = map(int, input().split())
a_n = list(map(int, input().split()))
b_m = list(map(int, input().split()))


s_a = sorted(a_n)
s_b = sorted(b_m)

a_idx = 0
b_idx = 0
cnt = 0
while b_idx < m and a_idx < n:
    if s_b[b_idx] <= s_a[a_idx]:
        cnt += s_a[a_idx]
        b_idx += 1
        a_idx += 1
    else:
        a_idx += 1


if b_idx < m:
    print(-1)
else:
    print(cnt)
