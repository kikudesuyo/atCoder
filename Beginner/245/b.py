n = int(input())
a_n = list(map(int, input().split()))
candidates = [i for i in range(0, 2001)]
for i in range(n):
    if a_n[i] in candidates:
        candidates.remove(a_n[i])
print(min(candidates))
