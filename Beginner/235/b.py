n = int(input())
h_n = list(map(int, input().split()))

idx = 0
while True:
    if idx == n - 1:
        print(h_n[idx])
        break
    if h_n[idx] < h_n[idx + 1]:
        idx += 1
    else:
        print(h_n[idx])
        break
