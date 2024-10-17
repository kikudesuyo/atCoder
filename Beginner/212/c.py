n, m = map(int, input().split())
a_n = list(map(int, input().split()))
b_m = list(map(int, input().split()))

sorted_an = sorted(a_n)
sorted_bm = sorted(b_m)

diff = 10**9

a_idx = 0
b_idx = 0
while True:
    if diff == 0:
        break
    if a_idx == n - 1 and b_idx == m - 1:
        diff = min(diff, abs(sorted_an[a_idx] - sorted_bm[b_idx]))
        break
    if a_idx == n - 1:
        diff = min(diff, abs(sorted_an[a_idx] - sorted_bm[b_idx]))
        b_idx += 1
        continue
    if b_idx == m - 1:
        diff = min(diff, abs(sorted_an[a_idx] - sorted_bm[b_idx]))
        a_idx += 1
        continue
    if abs(sorted_an[a_idx] - sorted_bm[b_idx]) < abs(
        sorted_an[a_idx] - sorted_bm[b_idx + 1]
    ):
        diff = min(diff, abs(sorted_an[a_idx] - sorted_bm[b_idx]))
        a_idx += 1
    else:
        diff = min(diff, abs(sorted_an[a_idx] - sorted_bm[b_idx + 1]))
        b_idx += 1


print(diff)
