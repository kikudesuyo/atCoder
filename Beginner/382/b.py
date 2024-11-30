n, d = map(int, input().split())
s = list(input())

r_s = s[::-1]

cnt = 0
i = 0
while cnt < d:
    if r_s[i] == "@":
        cnt += 1
        r_s[i] = "."
    i += 1

print("".join(r_s[::-1]))
