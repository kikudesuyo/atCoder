n = int(input())
a_s = list(map(int, input().split()))

answer = 0
while True:
    sorted_a = sorted(a_s, reverse=True)
    count = 0
    for i in range(n):
        if sorted_a[i] >= 1:
            count += 1
    if count <= 1:
        print(answer)
        exit()
    a_s = [sorted_a[0] - 1] + [sorted_a[1] - 1] + sorted_a[2:]
    answer += 1
