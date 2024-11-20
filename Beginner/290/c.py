n, k = map(int, input().split())
a_n = list(map(int, input().split()))

sorted_a_n = sorted(set(a_n))
k = min(k, len(sorted_a_n))

cnt = 0
while cnt < k:
    if cnt != sorted_a_n[cnt]:
        print(cnt)
        exit()
    cnt += 1
print(cnt)
