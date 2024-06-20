q = int(input())
queries = []

for _ in range(q):
    type, command = map(int, input().split())
    queries.append([type, command])
a_s = []
for type, command in queries:
    if type == 1:
        a_s.append(command)
    else:
        idx = len(a_s) - command
        print(a_s[idx])
