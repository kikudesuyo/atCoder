n = int(input())
a_n = list(map(int, input().split()))
called_people = [False] * n
for i in range(n):
    if called_people[i]:
        continue
    called_people[a_n[i] - 1] = True
print(called_people.count(False))
members = [i + 1 for i in range(n) if not called_people[i]]
print(" ".join(map(str, members)))
