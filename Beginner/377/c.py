n, m = map(int, input().split())
ab_m = [list(map(int, input().split())) for _ in range(m)]


def c(
    a,
    b,
    n,
):
    raw = [
        (a, b),
        (a - 2, b + 1),
        (a - 2, b - 1),
        (a - 1, b + 2),
        (a - 1, b - 2),
        (a + 1, b + 2),
        (a + 1, b - 2),
        (a + 2, b + 1),
        (a + 2, b - 1),
    ]
    valid_moves = [(x, y) for x, y in raw if 1 <= x <= n and 1 <= y <= n]
    return valid_moves


arr = []
for ab in ab_m:
    a, b = ab
    c_arr = c(a, b, n)
    arr.extend(c_arr)

total = n * n
print(total - len(set(arr)))
