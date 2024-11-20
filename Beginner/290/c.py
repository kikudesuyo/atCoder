n, k = map(int, input().split())
a_n = list(map(int, input().split()))

sorted_a_n = sorted(set(a_n))
key_num = len(sorted_a_n)
if k >= key_num:
    k = key_num
slice = sorted_a_n[:k]

cnt = 0
for i in slice:
    if cnt != i:
        print(cnt)
        exit()
    cnt += 1

print(cnt)
