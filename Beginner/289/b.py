n, m = map(int, input().split())
a_m = list(map(int, input().split()))

if m == 0:
    print(*list(range(1, n + 1)))
    exit()
if m == 1:
    answers = (
        [i for i in range(1, a_m[0])]
        + [a_m[0] + 1, a_m[0]]
        + [i for i in range(a_m[0] + 2, n + 1)]
    )
    print(*answers)
    exit()

continuouses = []
tmp = []
for i in range(m - 1):
    if a_m[i] + 1 == a_m[i + 1]:
        tmp.append(a_m[i])
    else:
        tmp.append(a_m[i])
        continuouses.append(tmp)
        tmp = []

if len(tmp) > 0:
    continuouses.append(tmp + [a_m[-1]])
if a_m[-2] + 1 != a_m[-1]:
    continuouses.append([a_m[-1]])

answers = []
current_num = 1
reversed_nums = []
for continuous in continuouses:
    tmp = continuous + [continuous[-1] + 1]
    reversed_nums.append(tmp[::-1])


tmp = []
for i in reversed_nums:
    tmp += i
not_continuouses = []
for i in range(1, n + 1):
    if i not in tmp:
        not_continuouses.append(i)

answers = []
current_num = 1
idx = 0
while len(answers) < n:
    if not current_num in tmp:
        answers.append(current_num)
        current_num += 1
    else:
        for i in reversed_nums[idx]:
            answers.append(i)
        current_num += len(reversed_nums[idx])
        idx += 1
print(*answers)
