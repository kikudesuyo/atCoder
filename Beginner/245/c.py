# DPを用いた解説AC

n, k = map(int, input().split())
a_n = list(map(int, input().split()))
b_n = list(map(int, input().split()))

dp = [[False, False] for _ in range(n)]  # 到達可能かどうか [0: a, 1: b]
dp[0][0] = dp[0][1] = True

for i in range(n - 1):
    if dp[i][0]:
        if abs(a_n[i] - a_n[i + 1]) <= k:
            dp[i + 1][0] = True
        if abs(a_n[i] - b_n[i + 1]) <= k:
            dp[i + 1][1] = True
    if dp[i][1]:
        if abs(b_n[i] - a_n[i + 1]) <= k:
            dp[i + 1][0] = True
        if abs(b_n[i] - b_n[i + 1]) <= k:
            dp[i + 1][1] = True

if dp[n - 1][0] or dp[n - 1][1]:
    print("Yes")
else:
    print("No")


# 自力AC
# from collections import deque

# n, k = map(int, input().split())
# a_n = list(map(int, input().split()))
# b_n = list(map(int, input().split()))

# d = deque(set())

# d.append((a_n[0], 0))
# d.append((b_n[0], 0))


# a_visited = [False] * n
# b_visited = [False] * n
# while d:
#     x_i, x_i_count = d.popleft()
#     if x_i_count == n - 1:
#         print("Yes")
#         exit()
#     if abs(x_i - a_n[x_i_count + 1]) <= k and not a_visited[x_i_count]:
#         d.append((a_n[x_i_count + 1], x_i_count + 1))
#         a_visited[x_i_count] = True
#     if abs(x_i - b_n[x_i_count + 1]) <= k and not b_visited[x_i_count]:
#         d.append((b_n[x_i_count + 1], x_i_count + 1))
#         b_visited[x_i_count] = True

# print("No")
