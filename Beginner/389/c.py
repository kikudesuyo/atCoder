q = int(input())
queries = [input() for _ in range(q)]


snakes = []
cnt = 0
retired_length = 0
sums = [0]
for r_query in queries:
    query = list(map(int, r_query.split()))
    if query[0] == 1:
        snakes.append(query[1])
        sums.append(sums[-1] + query[1])
    elif query[0] == 2:
        retired_length += snakes[cnt]
        cnt += 1
    elif query[0] == 3:
        print(sums[cnt + query[1] - 1] - retired_length)
        # print(snakes[cnt + query[1] - 1] - retired_length)
