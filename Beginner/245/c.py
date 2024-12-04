from collections import deque

n, k = map(int, input().split())
a_n = list(map(int, input().split()))
b_n = list(map(int, input().split()))

d = deque(set())

d.append((a_n[0], 0))
d.append((b_n[0], 0))


a_visited = [False] * n
b_visited = [False] * n
while d:
    x_i, x_i_count = d.popleft()
    if x_i_count == n - 1:
        print("Yes")
        exit()
    if abs(x_i - a_n[x_i_count + 1]) <= k and not a_visited[x_i_count]:
        d.append((a_n[x_i_count + 1], x_i_count + 1))
        a_visited[x_i_count] = True
    if abs(x_i - b_n[x_i_count + 1]) <= k and not b_visited[x_i_count]:
        d.append((b_n[x_i_count + 1], x_i_count + 1))
        b_visited[x_i_count] = True

print("No")
