### 木構造を考えて解く
n = int(input())
a_n = list(map(int, input().split()))

ans = [0] * (2 * n + 1)
for i in range(n):
    num = i + 1
    a = a_n[i]
    ans[num * 2 - 1] = ans[a - 1] + 1
    ans[num * 2] = ans[a - 1] + 1

print("\n".join(map(str, ans)))
