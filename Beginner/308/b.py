n, m = map(int, input().split())
c_n = input().split()
d_m = input().split()
p_m = list(map(int, input().split()))
dish_dict = {}
for i in range(m):
    dish_dict[d_m[i]] = p_m[i + 1]
count = 0
for dish in c_n:
    if dish in dish_dict.keys():
        count += dish_dict[dish]
    else:
        count += p_m[0]
print(count)
