from itertools import product

n, k = map(int, input().split())
r_s = list(map(int, input().split()))


arrays = []
for idx in range(len(r_s)):
    array = []
    for i in range(1, r_s[idx] + 1):
        array.append(i)
    arrays.append(array)


combinations = list(product(*arrays))

outputs = []
for combination in combinations:
    if sum(combination) % k == 0:
        string = "".join([str(i) for i in combination])
        outputs.append(string)
soterd_outputs = sorted(outputs)
for output in soterd_outputs:
    print(*output)
