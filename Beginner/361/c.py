n, k = map(int, input().split())
a_n = list(map(int, input().split()))

a_sort = sorted(a_n)

# 消すべき配列の優先度を決める
# 小さい数を消すべきか、大きい数を消すべきか
# それぞれ次の数を見てその差を確認する
asc_idx, desc_idx = 0, n - 1
priority = 0
priority_to_delete = []
for i in range(n):
    if desc_idx == 0 or asc_idx == n - 1:
        if desc_idx == n - 1:
            priority_to_delete.append(a_sort[asc_idx])
        else:
            priority_to_delete.append(a_sort[desc_idx])
        break
    ascend_diff = a_sort[asc_idx + 1] - a_sort[asc_idx]
    descending_diff = a_sort[desc_idx] - a_sort[desc_idx - 1]
    if ascend_diff > descending_diff:
        priority_to_delete.append(a_sort[asc_idx])
        asc_idx += 1
    else:
        priority_to_delete.append(a_sort[desc_idx])
        desc_idx -= 1
    priority += 1

splits = priority_to_delete[k:]
print(max(splits) - min(splits))
