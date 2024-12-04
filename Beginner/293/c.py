from itertools import combinations


def unique_permutations(row_move_num, col_move_num):
    total_moves = row_move_num + col_move_num
    row_positions = combinations(range(total_moves), row_move_num)
    results = []
    for row_pos in row_positions:
        move_arr = ["col"] * total_moves
        for i in row_pos:
            move_arr[i] = "row"
        results.append(tuple(move_arr))

    return results


h, w = map(int, input().split())
a_hw = [list(map(int, input().split())) for _ in range(h)]
move_vectors = [(0, 1), (1, 0)]
patterns = ["row", "col"]
p = unique_permutations(h - 1, w - 1)
cnt = 0
for move in p:
    set_num = [a_hw[0][0]]
    current = (0, 0)
    for m in move:
        if m == "row":
            current = (current[0] + 1, current[1])
        else:
            current = (current[0], current[1] + 1)
        set_num.append(a_hw[current[0]][current[1]])
    if len((set_num)) == len(set(set_num)):
        cnt += 1

print(cnt)
