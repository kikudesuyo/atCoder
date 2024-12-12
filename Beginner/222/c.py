n, m = map(int, input().split())
a_nm = [list(input()) for _ in range(n * 2)]

matrix_a_nm = list(zip(*a_nm))


def judge(player, opponent):
    if player == "G":
        if opponent == "C":
            return 1, 0
        elif opponent == "P":
            return 0, 1
        else:
            return 0, 0
    elif player == "C":
        if opponent == "P":
            return 1, 0
        elif opponent == "G":
            return 0, 1
        else:
            return 0, 0
    elif player == "P":
        if opponent == "G":
            return 1, 0
        elif opponent == "C":
            return 0, 1
        else:
            return 0, 0


data = []  # (point, player_num)
for i in range(n * 2):
    data.append((0, i))

for round in range(m):
    s_d = sorted(data, key=lambda x: (-x[0], x[1]))

    for j in range(0, n * 2, 2):
        r_1, idx_1 = s_d[j]
        r_2, idx_2 = s_d[j + 1]
        p1_hand = matrix_a_nm[round][idx_1]
        p2_hand = matrix_a_nm[round][idx_2]
        result = judge(p1_hand, p2_hand)
        data[j] = (r_1 + result[0], idx_1)
        data[j + 1] = (r_2 + result[1], idx_2)

s_d = sorted(data, key=lambda x: (-x[0], x[1]))

for point, i in s_d:
    print(i + 1)
