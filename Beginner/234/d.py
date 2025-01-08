import heapq

n, k = map(int, input().split())
p_n = list(map(int, input().split()))

arr = p_n[:k]
heapq.heapify(arr)
print(arr[0])
for i in range(k, n):
    # 一つ前の状態の最小値を出力している(新しく追加された値が最小値になるかどうかを確認するため)
    heapq.heappush(arr, p_n[i])  # 追加
    heapq.heappop(arr)  # 最小値取り出し
    print(arr[0])
