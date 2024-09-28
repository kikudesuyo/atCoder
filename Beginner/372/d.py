from bisect import bisect_left, bisect_right

n = int(input())
h_s = list(map(int, input().split()))


sorted_hs = sorted(h_s)

ranks = []
for i in range(n):
    left = bisect_left(sorted_hs, h_s[i])
    ranks.append(left)


answers = []
for idx in range(len(ranks)):
    if idx == 0:
        temp_idx = 0
        init_count = 0
        now_num = 0
        while temp_idx < len(ranks):
            if ranks[temp_idx] < now_num:
                now_num = ranks[temp_idx]
                init_count += 1
            else:
                temp_idx += 1
    if ranks[idx] < ranks[idx + 1] < ranks[idx - 1]:
        answers.append(-1)
    if ranks[idx] > ranks[idx + 1] > ranks[idx - 1]:
        answers.append(-1)
