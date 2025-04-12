n = int(input())
s_n = [input() for _ in range(n)]

is_auth = False
cnt = 0
for s in s_n:
    if s == "login":
        is_auth = True
    elif s == "logout":
        is_auth = False
    elif s == "private" and not is_auth:
        cnt += 1
print(cnt)
