n = int(input())

if n >= 42:
    print("AGC0" + str(n + 1))
else:
    print("AGC" + str(n).zfill(3))
