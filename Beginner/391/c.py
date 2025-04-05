from collections import defaultdict

n, q = map(int, input().split())
queries = [input() for _ in range(q)]

p_to_nest = defaultdict(int)
for i in range(n):
    p_to_nest[i + 1] = i + 1


nest_p_numbers = defaultdict(int)
for i in range(n):
    nest_p_numbers[i + 1] = 1

cnt = 0
for r_q in queries:
    query = list(map(int, r_q.split()))
    if query[0] == 1:
        p, h = query[1], query[2]
        current_place = p_to_nest[p]
        nest_p_numbers[current_place] -= 1
        if nest_p_numbers[current_place] == 1:
            cnt -= 1
        p_to_nest[p] = h
        nest_p_numbers[h] += 1
        if nest_p_numbers[h] == 2:
            cnt += 1
    elif query[0] == 2:
        print(cnt)
