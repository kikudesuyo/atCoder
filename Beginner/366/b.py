n = int(input())
s_n = [input() for _ in range(n)]
max_length = 0
for i in range(n):
    max_length = max(max_length, len(s_n[i]))

results = {}
for idx, string in enumerate(reversed(s_n)):
    for i in range(max_length):
        if not i in results.keys():
            results[i] = ""
        if i >= len(string):
            results[i] += "*"
        else:
            results[i] += string[i]

result_list = []
for i in results:
    result_list.append(results[i])


for result in result_list:
    while True:
        if result[-1] == "*":
            result = result[:-1]
        else:
            break
    print(result)
