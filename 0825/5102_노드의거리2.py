def bfs(g,s,e,v):
    # 그래프, 시작, 목표(끝), 정점의 개수

    visited = [False]*(v+1)
    q = []
    distance = 0 # 정점간의 거리
    q.append(s)
    visited[s] = True
    while q:
        # 몇 번 반복을 할 지 정해놓고 반복을 하면
        # 해다 단계에서 반복을 제한할 수 있다.
        size = len(q)
        distance += 1
        for _ in range(size):
            t = q.pop(0)
            for i in g[t]: # 인접리스트를 통해서 구한 t번 정점을 모두 탐색한다.
                if not visited[i]: # i번 정점을 방문한 적이 없다면
                    # i 번 정점이 내가 목표로 하는 정점이면, 거리를 리턴
                    if i == e:
                        return distance
                    q.append(i)
                    visited[i] = True
    return 0



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

    print(f"#{tc} {bfs(adjlist,S,G,V)}")
