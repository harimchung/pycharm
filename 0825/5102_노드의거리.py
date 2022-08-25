def bfs(g, s, e):
    # g는 인접리스트, s는 시작점, e는 도착점을 의미한다.
    visited = [0] * (V + 1)
    queue = []
    ans = V

    # 현재 위치를 visited에 추가하고, queue에도 추가한다.
    visited[s] = 1
    queue.append(s)

    # 현재 위치에서 방문할 수 있는 곳 탐색
    while queue:
        s = queue.pop(0)

        if s == e:
            r = visited[s] - 1
            if ans > r:
                ans = r

        for i in g[s]:
            if not visited[i]:
                queue.append(i)
                visited[i] = visited[s] + 1
    if ans == V:
        return 0
    return ans

T = int(input())
for tc in range(1,T+1):
    V, E = map(int, input().split())
    adjlist = [[] for _ in range(V+1)]

    # 인접리스트 만들기 (양방향)
    for _ in range(E):
        a, b = map(int, input().split())
        adjlist[a].append(b)
        adjlist[b].append(a)

    # 시작, 도착 노드
    S, G = map(int, input().split())

    print(f"#{tc} {bfs(adjlist,S,G)}")
