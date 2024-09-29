n = int(input())
c_n = []
a_nn = []
for i in range(n):
    c_i = int(input())
    a_in = list(map(int, input().split()))
    c_n.append(c_i)
    a_nn.append(a_in)
x = int(input())


num_dict = {}
for i in range(n):
    if x in a_nn[i]:
        if not c_n[i] in num_dict:
            num_dict[c_n[i]] = [i + 1]
        else:
            num_dict[c_n[i]].append(i + 1)


if len(num_dict) == 0:
    print(0)
    exit()
min_key = min(num_dict.keys())
print(len(num_dict[min_key]))
print(*num_dict[min_key])
