a, b, c, d, e, f, x = map(int, input().split())


def calc_score(a, b, c, x):
    score = 0
    a_count, c_count = 0, 0
    is_walking = True
    for _ in range(x):
        if is_walking:
            if a_count < a:
                a_count += 1
                score += b
        else:
            if c_count < c:
                c_count += 1
        if a_count == a:
            is_walking = False
            a_count = 0
        if c_count == c:
            is_walking = True
            c_count = 0
    return score


takahashi = calc_score(a, b, c, x)
aoki = calc_score(d, e, f, x)

if takahashi > aoki:
    print("Takahashi")
elif takahashi == aoki:
    print("Draw")
else:
    print("Aoki")
