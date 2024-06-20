a, b, d = map(int, input().split())

arr = [a]
elem = a
while True:
    if elem == b:
        break
    elem += d
    arr.append(elem)

print(*arr, sep=" ")
