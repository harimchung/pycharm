import sys

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def worm(si, sj, g):
    q = []
    q.append((si, sj))

    while q:
        i, j = q.pop(0)
        si, sj = i, j
        for d in range(4):
            ni, nj = si + di[d], sj +dj[d]
            if 0 <= ni < n and 0 <= nj < m and g[ni][nj] == 1:
                q.append((ni,nj))
                g[ni][nj] = 0




T = int(sys.stdin.readline())
for _ in range(T):
    m, n, k = map(int, sys.stdin.readline().split())

    arr = [[0]*m for _ in range(n)]

    for _ in range(k):
        a, b = map(int, sys.stdin.readline().split())
        arr[b][a] = 1

    worms = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                worm(i, j, arr)
                worms += 1

    print(worms)