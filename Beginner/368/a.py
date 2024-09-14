n, k = map(int, input().split())
a_s = list(map(int, input().split()))

answers = a_s[(-1) * k :] + a_s[: (-1) * k]

print(" ".join(map(str, answers)))
