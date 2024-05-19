n = int(input())

a_cards = []
a_idx_dict = {}
n_list = []
a_key_dict = {}
c_key_dict = {}
for i in range(n):
    a, s = list(map(int, input().split()))
    a_cards.append(a)
    a_key_dict[a] = s
    c_key_dict[s] = a
    a_idx_dict[a] = i
    n_list.append(i + 1)
a_sort = sorted(a_cards)
a_key_sorted_dict = {key: a_key_dict[key] for key in a_sort}
removed_arr = []
for sorted_idx, a_i in enumerate(a_sort):
    now_c = a_key_sorted_dict[a_i]
    next_c = a_key_sorted_dict[a_sort[sorted_idx + 1]]
    if now_c > next_c:
        removed_a_i = c_key_dict[now_c]
        removed_idx = a_idx_dict[removed_a_i]
        removed_arr.append(removed_idx + 1)
    if sorted_idx == n - 2:
        break

print(n - len(removed_arr))
for i in n_list:
    if i not in removed_arr:
        print(i, end=" ")
print()
# result_list = [str(item) for item in n_list if item not in removed_arr]

# print(len(result_list))
# print(" ".join(result_list))
