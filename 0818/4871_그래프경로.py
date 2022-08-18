# 첫 줄에는 테스트케이스의 개수 T가 주어진다.
T = int(input())

for tc in range(1,T+1):
    # 연결되어있으면 1이라고 출력한다.
    ans = 1
    # 인접한 리스트를 먼저 만든다.
    adj = [[] for _ in range (50)]
    # 다음 줄부터 테스트 케이스의 첫줄에 V와 E가 주어진다.
    V, E = map(int, input().split())

    # 테스트케이스의 두번째 줄부터 E줄에 걸쳐서 출발 도착 노드가 간선 정보가 주어진다.
    for _ in range(E):
        # 간선이 연결된 정보가 E 의 개수만큼 들어온다.
        a, b = map(int, input().split())
        adj[a].append(b)

    # E 개의 줄 이후에는 경로의 존재를 확인할 출발 노드 S와 도착노드 G가 주어진다.
    S, G = map(int, input().split())
    stack = []

    # 방문했는지를 체크할 visited 를 만든다.
    # 만약 방문했으면 1로 바꾼다. 인덱스의 편의성을 위해 V+1 크기만큼 만든다.
    visited = [0]*(V+1)

    # 시작점 S를 visited에 갔다고 표시한다.
    visited[S] = 1
    # while True:
    while True:
        if S == G:
            break

        for j in adj[S]:
        # 인접리스트에 있는 원소로 이동한다.
            # 가지 않은 원소가 있다면 그 원소로 이동한다.
            if visited[j] == 0:
            # stack 리스트에 원소를 추가한다.
                stack.append(j)
            # 시작점 S는 원소의 값으로 바뀐다.
                S = j
                visited[S] = 1

                break

        # 만약 갈 수 있는 w가 없으면,
        else:
            # 만약 S ==G 인 경우 끝내부러

            # 스택이 비어있지 않은 경우
            if stack:
                # 한칸 뒤로움직인다.
                b = stack.pop(-1)
                S = b
            # 스택이 비어있으면
            else:
                ans = 0
                break
                #break

    print(f"#{tc} {ans}")
