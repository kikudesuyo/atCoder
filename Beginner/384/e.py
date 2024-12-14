import heapq

h, w, x = map(int, input().split())
p, q = map(int, input().split())

s_hw = [list(map(int, input().split())) for _ in range(h)]

vectors = [(1, 0), (-1, 0), (0, 1), (0, -1)]

cur_strength = s_hw[p - 1][q - 1]
visited = [[False] * w for _ in range(h)]
visited[p - 1][q - 1] = True

heap = []
for vector in vectors:
    new_position = (p - 1 + vector[0], q - 1 + vector[1])
    if 0 <= new_position[0] < h and 0 <= new_position[1] < w:
        heapq.heappush(heap, (s_hw[new_position[0]][new_position[1]], new_position))

while heap:
    slime, position = heapq.heappop(heap)
    if cur_strength > slime * x and not visited[position[0]][position[1]]:
        cur_strength += slime
        visited[position[0]][position[1]] = True
        for vector in vectors:
            new_position = (position[0] + vector[0], position[1] + vector[1])
            if (
                0 <= new_position[0] < h
                and 0 <= new_position[1] < w
                and not visited[new_position[0]][new_position[1]]
            ):
                heapq.heappush(
                    heap, (s_hw[new_position[0]][new_position[1]], new_position)
                )

print(cur_strength)
