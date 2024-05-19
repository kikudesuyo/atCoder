n = int(input())
a_s = list(map(int, input().split()))
sorted_a_s = sorted(a_s)
threshold = 10**8
count = 0
left, right = 0, n - 1
# leftとrightを近づけてカウントをする。
while left <= right:
    if sorted_a_s[left] + sorted_a_s[right] >= threshold:
        right -= 1
    else:
        left += 1
        # rightの次の値からnまでの値は条件を満たす(インデックスを基に記述)
        count += (n - 1) - (right + 1) + 1
# 残りのleftはleft<rightであれば全て条件を満たす
# leftがn-1まで全て満たす
rest = n - left - 1
count += (rest * (rest + 1)) // 2
total = sum(a_s) * (n - 1)
print(total - (count * threshold))
