s = list(input())


cnt = 0
for i in range(len(s) - 1):
    if s[i : i + 2] == ["i", "i"]:
        cnt += 1
    elif s[i : i + 2] == ["o", "o"]:
        cnt += 1


if s[0] != "i":
    cnt += 1

if (cnt + len(s)) % 2 == 0:
    print(cnt)
else:
    print(cnt + 1)
