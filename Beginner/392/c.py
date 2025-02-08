n = int(input())
p_n = list(map(int, input().split()))
q_n = list(map(int, input().split()))


zekken_to_me = {}
me_to_zekken = {}
me_to_opponent = {}
for i in range(n):
    me_to_opponent[i + 1] = p_n[i]
    zekken_to_me[q_n[i]] = i + 1
    me_to_zekken[i + 1] = q_n[i]


ans = []
for i in range(n):
    me = zekken_to_me[i + 1]
    opponent = me_to_opponent[me]
    opponent_zekken = me_to_zekken[opponent]
    ans.append(opponent_zekken)

print(*ans)
