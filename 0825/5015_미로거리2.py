T = int(input())

for tc in range(1, T+1):
    n = int(input())

    maze = [list(map(int, input())) for _ in range(n)]

    si = sj = 0

    # 시작위치 (값이 2인 위치를 찾기)
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                si = i
                sj = j

    q = []
    # 큐 초기화
    # 시작위치에 넣고, 방문체크
    q.append((si, sj))
    maze[si][sj] = 1 # 내가 갔던 위치는 벽으로 만들어서 다음에 방문하지 못하도록 한다.
    distance = -1

    di = [-1, 1, 0, 0]
    dj = [0, 0 , -1, 1]

    find = False # 중간에 도착지점을 찾으면 True -> 반복문을 종료시킬 인자가 필요하다.

    while q and not find:
        size = len(q)
        distance += 1
        for _ in range(size):
            i, j = q.pop(0)
            for d in range(4):
                ni = i+di[d]
                nj = j+dj[d]

                if 0<= ni <n and 0<= nj <n and maze[ni][nj] != 1:
                    # 만약 다음위치가 방문 가능한데, 도착지점일 경우
                    if maze[ni][nj] == 3:
                        q = []
                        find = True
                        break

                    maze[ni][nj] = 1
                    q.append((ni,nj))
            if find:
                break

        if not find:
            distance = 0

    print(f"#{tc} {distance}")
