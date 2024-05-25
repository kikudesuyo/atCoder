a, b = list(map(int, input().split()))


list = [1, 2, 3]
if a == b:
    print(-1)
else:
    list.remove(a)
    list.remove(b)
    print(list[0])
