n = int(input())

max_idx = 0
max_head = 0
max_whole_body = 0
titan_sholders = []
for i in range(n):
    sholder, whole_body = list(map(int, input().split()))
    titan_sholders.append(sholder)
    if whole_body - sholder >= max_head:
        max_idx = i
        max_head = whole_body - sholder
        max_whole_body = whole_body
titan_sholders.pop(max_idx)
print(sum(titan_sholders) + max_whole_body)
