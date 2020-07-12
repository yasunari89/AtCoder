n, q = map(int, input().split())
queries = []
for _ in range(q):
    queries.append(list(map(int, input().split())))

parent = [i for i in range(n)]

def root(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = root(parent[x])
        return parent[x]

def same(x, y):
    return root(x) == root(y)

def unite(x, y):
    x = root(x)
    y = root(y)
    if (x == y):
        return
    parent[x] = y

q = vertexa = vertexb = 0
for query in queries:
    q, vertexa, vertexb = map(int, query)
    if q:
        boolean = same(vertexa, vertexb)
        if boolean:
            print('Yes')
        else:
            print('No')
    else:
        unite(vertexa, vertexb)