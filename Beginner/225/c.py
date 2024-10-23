n, m = map(int, input().split())
b_nm = [list(map(int, input().split())) for _ in range(n)]


def qr(num, divisor):
    return num // divisor, num % divisor


base_q, base_r = qr(b_nm[0][0], 7)
if base_r == 0:
    base_r = 7
    base_q -= 1

q, r = base_q, base_r
for row in range(n):
    for col in range(m):
        cur_q, cur_r = qr(b_nm[row][col], 7)
        if cur_r == 0:
            cur_r = 7
            cur_q -= 1
        if cur_q == q and cur_r == r:
            r += 1
        else:
            print("No")
            exit()
    q += 1
    r = base_r
print("Yes")
