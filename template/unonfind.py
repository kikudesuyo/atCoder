class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    # def find(self, x):
    #     if self.parent[x] == x:
    #         return x
    #     self.parent[x] = self.find(self.parent[x])
    #     return self.parent[x]

    # def unite(self, x, y):
    #     root_x = self.find(x)
    #     root_y = self.find(y)
    #     if root_x == root_y:
    #         return
    #     if self.rank[root_x] < self.rank[root_y]:
    #         self.parent[root_x] = root_y
    #     elif self.rank[root_x] > self.rank[root_y]:
    #         self.parent[root_y] = root_x
    #     else:
    #         self.parent[root_x] = root_y
    #         self.rank[root_y] += 1

    # def is_same(self, x, y):
    #     return self.find(x) == self.find(y)
