n = int(input())

max_num = 2 * n + 1

n_list = [False] * max_num

for _ in range(n):
    for i in range(max_num):
        if not n_list[i]:
            n_list[i] = True
            print(i + 1, flush=True)
            break
    aoki_input = int(input())
    n_list[aoki_input - 1] = True

for i in range(len(n_list)):
    if not n_list[i]:
        print(i + 1, flush=True)

print(0)
