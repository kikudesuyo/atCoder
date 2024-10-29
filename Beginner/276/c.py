n = int(input())
p_n = list(map(int, input().split()))


idx = 0
for i in range(n - 1):
    if p_n[i] > p_n[i + 1]:
        idx = i

sec_arr = p_n[idx:]
top = 0
for i in range(len(sec_arr)):
    if sec_arr[i] < sec_arr[0]:
        top = max(sec_arr[i], top)
sec_arr.remove(top)
sec_ans_arr = [top] + sorted(sec_arr, reverse=True)


ans = p_n[:idx] + sec_ans_arr
print(*ans)
