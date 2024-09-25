n, p, q, r, s = map(int, input().split())
a_n = list(map(int, input().split()))

p_q = a_n[p - 1 : q]
r_s = a_n[r - 1 : s]

a_n[r - 1 : s] = p_q
a_n[p - 1 : q] = r_s
print(*a_n)
