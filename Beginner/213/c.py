from bisect import bisect_left

h, w, n = map(int, input().split())
ab_n = [list(map(int, input().split())) for _ in range(n)]

rows = [ab_n[i][0] for i in range(n)]
cols = [ab_n[i][1] for i in range(n)]

# その数自身に重複があっても問題ないが、それ以前に重複があるとズレる。 setを用いて重複を削除
r_sort = sorted(set(rows))
c_sort = sorted(set(cols))

for i in range(n):
    r_pos = bisect_left(r_sort, ab_n[i][0]) + 1  # 左側のインデックスを返す
    c_pos = bisect_left(c_sort, ab_n[i][1]) + 1
    print(r_pos, c_pos)
