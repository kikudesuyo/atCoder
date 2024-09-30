n = int(input())
a_n = list(map(int, input().split()))


cuts = [0]
for a in a_n:
    cuts = [(cut + a) % 360 for cut in cuts]
    cuts.append(0)

sorted_cuts = sorted(cuts) + [360]

max_diff = 0
for i in range(len(sorted_cuts) - 1):
    diff = sorted_cuts[i + 1] - sorted_cuts[i]
    max_diff = max(max_diff, diff)
print(max_diff)
