from collections import deque

n = int(input())
t_nk = [list(map(int, input().split())) for _ in range(n)]

target_skills = t_nk[-1][2:]

d = deque()
for i in target_skills:
    d.append(i)

visited = [False] * n
cnt = 0
while d:
    skill_idx = d.popleft() - 1
    if visited[skill_idx]:
        continue
    cnt += t_nk[skill_idx][0]
    visited[skill_idx] = True
    skills = t_nk[skill_idx][2:]
    for s in skills:
        if not visited[s - 1]:
            d.append(s)

cnt += t_nk[-1][0]
print(cnt)
