n = int(input())
a_n = list(map(int, input().split()))

soreted_a_n = sorted(a_n)

temp = soreted_a_n[0]
for i in range(1, len(soreted_a_n)):
    if temp + 1 != soreted_a_n[i]:
        print(temp + 1)
        exit()
    else:
        temp += 1
