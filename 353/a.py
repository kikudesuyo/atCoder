n = int(input())
h_s = list(map(int, input().split()))
for i in range(1, len(h_s)):
    if h_s[0] < h_s[i]:
        print(i + 1)
        exit()
print(-1)
