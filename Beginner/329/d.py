from collections import defaultdict

n, m = map(int, input().split())
a_m = list(map(int, input().split()))

d = defaultdict(int)

current_winner = 0
current_num = 0
for i in range(m):
    candidate = a_m[i]
    d[candidate] += 1
    if d[candidate] > current_num:
        current_num = d[candidate]
        current_winner = candidate
    elif current_winner != candidate and d[candidate] == current_num:
        if candidate < current_winner:
            current_winner = candidate
    print(current_winner)
