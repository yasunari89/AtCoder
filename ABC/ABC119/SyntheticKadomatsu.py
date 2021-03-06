many, A, B, C = map(int, input().split())
bamboos = [int(input()) for i in range(many)]

# point: 訳が分からなくなるものは自分でルールづけをする
# 合成魔法を全て最初に行う、というルールづけ

# 解法: DFS or 4進数(4patternsで2の累乗だからできる)
# PS: DFS(深さ優先探索), BFS(幅優先探索)

infinity = 1e10

def dfs(depth, a, b, c):
    if depth == many:
        if min(a, b, c) > 0:
            # 竹が何もない状態でも各竹に+10がかかっていることから-30する必要がある。
            # また、+10が一個はないとベースとなる竹がないことになるので
            # a,b,c = 0はコストを無限にすることで避ける。
            return abs(a-A) + abs(b-B) + abs(c-C) - 30
        else:
            return infinity
    else:
        ret0 = dfs(depth+1, a, b, c)
        ret1 = dfs(depth+1, a+bamboos[depth], b, c) + 10
        ret2 = dfs(depth+1, a, b+bamboos[depth], c) + 10
        ret3 = dfs(depth+1, a, b, c+bamboos[depth]) + 10
        return min(ret0, ret1, ret2, ret3)

print(dfs(0, 0, 0, 0))
