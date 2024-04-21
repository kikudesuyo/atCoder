import collections

str_n, str_q = input().split(" ")
ts = list(map(int, input().split(" ")))
n, q = int(str_n), int(str_q)

counters = collections.Counter(ts)
count = n
# print(counters)
for i in range(1, 1001):
    if int(counters[i]) % 2 == 1:
        count += -1
print(count)
