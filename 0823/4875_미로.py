def dfs(i, j, N):
    visited = [[0]*N for _ in range(N)]

    stack = []

    di = [-1, 1, 0, 0]
    dj = [0, 0 ,-1, 1]


    while True:
        # 현재 위치를 방문했다고 체크한다.
        visited[i][j] = 1
        # 현재 i, j에서 갈 수 있는 곳을 탐색한다.
        # 2차원 배열에서는 상, 하, 좌, 우로 움직일 수 있다.
        if arr[i][j] == "3":
            return 1
            break

        for d in range(4):
            ni = di[d] + i
            nj = dj[d] + j
            # 다음 위치 정한 다음에 움직일 수 있는지 알아보기
            # 벽이면(1) 이면 못간다, 2차원 배열 벗어나도, 방문한 적 있는 좌표여도 못간다.
            if 0<= ni < N and 0 <= nj < N and arr[ni][nj] != "1" and visited[ni][nj] == 0:
                # 현재위치를 스택에 저장
                stack.append((i,j))
                # 현재 위치를 다음위치로 최신화
                i = ni
                j = nj
                break

        else:
            # pop()을 해서 뒤로 돌아간다.
            if stack:
                i, j = stack.pop()
            # 스택이 비어있으면 반복을 종료한다.
            else:
                return 0
                break


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(c for c in input()) for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if arr[i][j] == "2":
                break
    print(f"#{tc} {dfs(i,j,n)}")
