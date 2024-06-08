n = int(input())

level_1 = ["###", "#.#", "###"]
level_2 = [
    "#########",
    "#.##.##.#",
    "#########",
    "###...###",
    "#.#...#.#",
    "###...###",
    "#########",
    "#.##.##.#",
    "#########",
]


def blank(n):
    if n == 2:
        return "." * 3**n
    else:
        return [[blank(n - 1), blank(n - 1), blank(n - 1)]] * 3


level_3 = [
    level_2[0] * 3,
    level_2[1] * 3,
    level_2[2] * 3,
    level_2[3] * 3,
    level_2[4] * 3,
    level_2[5] * 3,
    level_2[6] * 3,
    level_2[7] * 3,
    level_2[8] * 3,
    level_2[0] + blank(2) + level_2[0],
    level_2[1] + blank(2) + level_2[1],
    level_2[2] + blank(2) + level_2[2],
    level_2[3] + blank(2) + level_2[3],
    level_2[4] + blank(2) + level_2[4],
    level_2[5] + blank(2) + level_2[5],
    level_2[6] + blank(2) + level_2[6],
    level_2[7] + blank(2) + level_2[7],
    level_2[8] + blank(2) + level_2[8],
    level_2[0] * 3,
    level_2[1] * 3,
    level_2[2] * 3,
    level_2[3] * 3,
    level_2[4] * 3,
    level_2[5] * 3,
    level_2[6] * 3,
    level_2[7] * 3,
    level_2[8] * 3,
]

print(*level_3, sep="\n")
