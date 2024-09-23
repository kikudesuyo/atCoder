n = int(input())
wx_s = [list(map(int, input().split())) for _ in range(n)]
# 日時が変わるときの問題は割り算の余りを使えば楽に書ける
works = [0] * 24
for w, x in wx_s:
    for i in range(9):
        works[(i + x) % 24] += w
print(max(works))
