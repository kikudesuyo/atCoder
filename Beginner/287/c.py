from collections import defaultdict
n,m = map(int, input().split())
uv_n = [list(map(int, input().split())) for _ in range(m)]

d = defaultdict(set)

for u,v in uv_n:
    d[u].add(v)
    d[v].add(u)

arr = []
for key, val in d.items():
    if len(val) == 1:
        arr.append(key)
    if len(val) >= 3:
        print("No")
        exit()

if len(arr) != 2:
    print("No")
    exit()
    
start,end = arr
current = start
visited = set() 
visited.add(start)
for i in range(m):
    for next in d[current]:
        if next not in visited:
            current = next
            visited.add(next)
            

if current == end and len(visited) == n:
    print("Yes")
else:
    print("No")

        
