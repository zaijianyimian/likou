import sys

input = sys.stdin.readline

sys.setrecursionlimit(300000)
parent = {}

def find(x):
    if x not in parent:
        parent[x] = x
    elif parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]
def union(x,y):
    rootx = find(x)
    rooty = find(y)
    if rootx != rooty:
        parent[rootx] = rooty
def solve():
    n,m,q = map(int,input().split())
    idx = 3
    edges = set()
    for _ in range(m):
        u,v = map(int,input().split())
        if u > v:
            u,v = v,u
        edges.add((u,v))
    queries = []
    deleteEdges = set()
    for _ in range(q):
        op,u,v = map(int,input().split())
        if u > v:
            u,v = v,u
        queries.append((op,u,v))
        if op == 1:
            deleteEdges.add((u,v))
    filalEdges = edges - deleteEdges
    for u,v in filalEdges:
        union(u,v)
    ans = []
    for i in range(q - 1,-1, -1):
        op,u,v = queries[i]
        if op == 2:
            if find(u) == find(v):
                ans.append("Yes")
            else:
                ans.append("No")
        else:
            if (u,v) in edges:
                union(u,v)
    ans.reverse()
    if ans:
        sys.stdout.write('\n'.join(ans)+'\n')
if __name__ == '__main__':
    solve()