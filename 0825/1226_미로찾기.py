di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

# bfs 로 풀이하기
def bfs(g, si, sj):
    visited = [[False] * 16 for _ in range(16)]
    queue = []
    queue.append((si,sj))
    visited[si][sj] = True


    while queue:
        i, j = queue.pop(0)
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]

            if 0<= ni < 16 and 0<= nj <16 and not visited[ni][nj]:
                if g[ni][nj] == 3:
                    return 1
                queue.append((ni,nj))
                visited[ni][nj] = True
    return 0

for _ in range(10) :
    tc = int(input())
    arr = [list(map(int, input())) for _ in range(16)]
    si=sj=0

    for i in range (16):
        for j in range (16):
            if arr[i][j] == 2:
                si = i
                sj = j
                break

    print(f"#{tc} {bfs(arr, si,sj)}")