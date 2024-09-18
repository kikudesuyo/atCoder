M, D = map(int, input().split())
y, m, d = map(int, input().split())

if D > d:
    print(y, m, d + 1)
else:
    if M > m:
        print(y, m + 1, 1)
    else:
        print(y + 1, 1, 1)
