h, w = map(int, input().split())
s_h = [list(input()) for _ in range(h)]
t_h = [list(input()) for _ in range(h)]


s = []
t = []
for i in range(h):
    tp_s = []
    tp_t = []
    for j in range(w):
        if s_h[i][j] == "#":
            tp_s.append(1)
        else:
            tp_s.append(0)
        if t_h[i][j] == "#":
            tp_t.append(1)
        else:
            tp_t.append(0)
    s.append(tp_s)
    t.append(tp_t)

mat_s = list(map(list, zip(*s)))
mat_t = list(map(list, zip(*t)))

sorted_mat_s = sorted(mat_s)
sorted_mat_t = sorted(mat_t)
if sorted_mat_s == sorted_mat_t:
    print("Yes")
else:
    print("No")
