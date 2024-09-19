from bisect import bisect_left, bisect_right

n = int(input())
a_s = list(map(int, input().split()))
q = int(input())
b_q = []
for i in range(q):
    b_q.append(int(input()))

sorted_a_s = sorted(a_s)


for b_j in b_q:
    idx = bisect_left(sorted_a_s, b_j)
    if idx == 0:
        print(abs(sorted_a_s[idx] - b_j))
        continue
    if idx == n:
        print(abs(sorted_a_s[idx - 1] - b_j))
        continue
    min_num = (
        abs(sorted_a_s[idx - 1] - b_j)
        if abs(sorted_a_s[idx - 1] - b_j) < abs(sorted_a_s[idx] - b_j)
        else abs(sorted_a_s[idx] - b_j)
    )
    print(min_num)
