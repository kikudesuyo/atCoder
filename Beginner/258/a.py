k = int(input())

h, m = k // 60, k % 60

print(str(21 + h) + ":" + (str(m).zfill(2)))
