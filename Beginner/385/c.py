n = int(input())
h_n = list(map(int, input().split()))

ans = 1
for interval in range(1, n):
    for start in range(interval):
        tmp = []
        for i in range(start, n, interval):
            tmp.append(h_n[i])
        current = tmp[0]
        cnt = 1
        m_cnt = 1
        for i in range(1, len(tmp)):
            if current == tmp[i]:
                cnt += 1
            else:
                m_cnt = max(m_cnt, cnt)
                cnt = 1
                current = tmp[i]
        m_cnt = max(m_cnt, cnt)
        ans = max(m_cnt, ans)
print(ans)
