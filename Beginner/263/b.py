n = int(input())
p_n = list(map(int, input().split()))

count = 0
idx = n - 2
for i in range(len(p_n)):
    if p_n[idx] == 1:
        print(count + 1)
        break
    idx = p_n[idx] - 2
    count += 1
