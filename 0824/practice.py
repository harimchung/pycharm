di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

# bfs
adjlist = [
        [],
        [2,3],
        [1,4,5],
        [1,7],
        [2,6],
        [4,5,7],
        [3,6],
]
def bfs(si, sj, n):
        # g는 인접리스트, v는 시작점, n은 점의 개수를 의미한다.
        visited = [[0]*n for _ in range(n)]
        queue = []

        visited[si][sj] = 1
        queue.append((si,sj))

        # 첫 위치를 append 했다면, queue가 차있다.
        # queue가 비어있지 않다면 계속 반복한다.
        day = 0
        while queue:
                # 방문할 위치는 큐에 들어있고, 그 위치의 개수를 구하면 된다.
                size = len(queue)

                print("=========")
                print(f"{day} 일차...")
                for k in range(n):
                        print(visited[k])
                print("=========")

                # 해당 일차에만 반복을 하도록 제한할 수 있다.
                for _ in range(size):
                        # 현재위치 pop
                        i, j = queue.pop(0)

                        # 현재 위치에서 방문할 수 있는 위치 탐색
                        for d in range(4):
                                ni = i+di[d]
                                nj = j+dj[d]
                        if 0<= ni <n and 0<= nj <n and not visited[ni][nj]:
                                visited[ni][nj] = 1
                                queue.append((ni, nj))
                day += 1
n = 10
bfs(5,5,10)
