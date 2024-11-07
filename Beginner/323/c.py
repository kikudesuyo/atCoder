from collections import defaultdict

n, m = map(int, input().split())
a_m = list(map(int, input().split()))
s_n = [list(input()) for _ in range(n)]


current_points = []
left_problems = defaultdict(list)  # key:user, val: left_problem scores
for i, user_scores in enumerate(s_n):
    cnt = i + 1
    for j, user_score in enumerate(user_scores):
        if user_score == "o":
            cnt += a_m[j]
        else:
            left_problems[i].append(a_m[j])

    current_points.append(cnt)

for i, current_point in enumerate(current_points):
    diff = max(current_points) - current_point
    if diff < 0:
        print(0)
    else:
        user_left_problems = sorted(left_problems[i], reverse=True)
        idx = 0
        cnt = 0
        while diff > 0:
            diff -= user_left_problems[idx]
            cnt += 1
            idx += 1
        print(cnt)
