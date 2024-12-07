n = int(input())
tv_n = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
idx = 0
i = 0
while i < tv_n[-1][0]:
    if tv_n[idx][0] > i:
        i += 1
        if cnt > 0:
            cnt -= 1
    if tv_n[idx][0] == i:
        cnt += tv_n[idx][1]
        idx += 1

print(cnt)
