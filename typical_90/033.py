h, w = map(int, input().split())

count = 0
if h == 1:
    count = w
elif w == 1:
    count = h
else:
    for i in range(h):
        for j in range(w):
            if i % 2 == 0 and j % 2 == 0:
                count += 1

print(count)
