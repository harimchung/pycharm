di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def maze(si,sj,n,g):
    # 미로에는 처음 시작점의 행과 열, nxn 에 대한 정보가 주어진다.
    visited = [[0]*n for _ in range(n)]
    q = []

    # 처음 위치를 방문했다고 표시한다.
    visited[si][sj] = 1
    q.append((si,sj))

    # q가 빌 때까지 진행한다.
    while q:
        i, j = q.pop(0)
        # 주변에 갈 곳이 있는지 탐색한다.

        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if 0<= ni <n and 0<= nj <n and g[ni][nj] != 1 and visited[ni][nj] == 0:
                q.append((ni,nj))
                visited[ni][nj] = visited[i][j] + 1
                if  g[ni][nj] == 3:
                    return visited[ni][nj] - 2
                    break

    return 0

T = int(input())
for tc in range (1, T+1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                si = i
                sj = j
                break


    print(f"#{tc} {maze(si,sj,n,arr)}")