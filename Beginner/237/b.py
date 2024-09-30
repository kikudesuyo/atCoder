h, w = map(int, input().split())
a_hw = [list(map(int, input().split())) for _ in range(h)]

transposed_a_hw = list(map(list, zip(*a_hw)))
for i in range(w):
    print(*transposed_a_hw[i])
