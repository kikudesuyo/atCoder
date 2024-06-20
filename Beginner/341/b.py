n = int(input())
a_s = list(map(int, input().split()))
st_s = []
for i in range(n - 1):
    s, t = map(int, input().split())
    st_s.append([s, t])

for i in range(n - 1):
    if i == n - 1:
        break
    exchanged_num = (a_s[i] // st_s[i][0]) * st_s[i][1]
    a_s[i + 1] += exchanged_num

print(a_s[-1])
