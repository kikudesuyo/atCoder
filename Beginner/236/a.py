s = list(input())
a, b = map(int, input().split())

a_str, b_str = s[a - 1], s[b - 1]

s[a - 1] = b_str
s[b - 1] = a_str


print("".join(s))
