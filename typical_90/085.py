k = int(input())


cnt = 0
a_max = int(k ** (1 / 3)) + 1
for a in range(1, a_max + 1):
    if k % a != 0:
        continue
    bc = k // a
    b_max = int(bc ** (1 / 2)) + 1
    for b in range(a, b_max + 1):
        if bc % b != 0:
            continue
        c = bc // b
        if a <= b <= c and a * b * c == k:
            cnt += 1

print(cnt)
