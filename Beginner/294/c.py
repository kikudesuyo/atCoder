from bisect import bisect_left

n, m = map(int, input().split())
a_n = list(map(int, input().split()))
b_m = list(map(int, input().split()))

c_nm = sorted(a_n + b_m)


ans_a = []
for a_elem in a_n:
    idx = bisect_left(c_nm, a_elem)
    ans_a.append(idx + 1)
ans_b = []
for b_elem in b_m:
    idx = bisect_left(c_nm, b_elem)
    ans_b.append(idx + 1)
print(*ans_a)
print(*ans_b)
