n, t = map(int, input().split())
c_n = list(map(int, input().split()))
r_n = list(map(int, input().split()))

if t in c_n:
    candidate_players = {}
    for i in range(n):
        if c_n[i] == t:
            candidate_players[r_n[i]] = i
    max_num = max(candidate_players.keys())
    print(candidate_players[max_num] + 1)
else:
    player_1_color = c_n[0]
    candidate_players = {}
    for i in range(n):
        if c_n[i] == player_1_color:
            candidate_players[r_n[i]] = i
    max_num = max(candidate_players.keys())
    print(candidate_players[max_num] + 1)
