from Errors import Errors

class UnionFind:
    
    def __init__(self, N):
        '''
        親の番号を格納する。親だった場合は-(その集合のサイズ)とする。
        作る時はparentの値を全て-1にすることで、全てバラバラになる。
        '''
        self.N = N
        self.parent = [-1 for i in range(self.N)]

    def root(self, A):
        'Aがどのグループに属しているか調べる。'
        if self.parent[A] < 0:
            return A
        else:
            self.parent[A] = self.root(self.parent[A])
            return self.parent[A]

    def size(self, A):
        '自分のいるグループの頂点数を調べる。'
        return -self.parent[self.root(A)]

    def connect(self, A, B):
        '''
        AとBをくっつける。
        AとBを直接繋ぐのではなく、root(A)にroot(B)をくっつける。
        '''
        A = self.root(A)
        B = self.root(B)
        if A == B:
            # すでにくっついているからくっつけない。
            return False
        elif self.size(A) < self.size(B):
            # 大小が逆だったらひっくり返す。
            A, B = B, A
        else:
            pass
        # Aのサイズを変更する。
        self.parent[A] += self.parent[B]
        # Bの親をAに変更する。
        self.parent[B] = A
        return True
