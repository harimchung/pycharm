# 인접한 리스트가 주어진다고 가정
adj=[
    [1,2],
    [0,3,4],
    [0,4],
    [1,5],
    [1,2,5],
    [6],
    [5]
]
def dfs (s,V):
    # s는 처음 시작하는 번호를 의미한다.
    # V는 마지막 번호를 의미한다.

    # 방문했는지를 표시할 리스트와
    visited = [True]*(V+1)      # 번호는 0번부터 있으므로 V+1개를 만든다.
    # 최종 방문한 위치를 표시할 스택이 필요하다.
    stack = []
    now = s                     # 현재 위치는 s부터 시작한다.
    while True:
        # 만약 인접한 리스트에 true인 숫자가 있다면
        for j in adj[now]:
            if j:
                # 그곳으로 이동하고, False로 바꾼다.
                visited[j] = False
                # now의 위치를 바꾼다.
                now = j
                print(now)
                # 스택에도 추가한다.
                stack.append(now)

        # 만약 인접한 리스트에 true인 숫자가 없다면
        else :
            # 스택이 빈 스택이 아닌경우,
            # 스택의 마지막 곳으로 now를 이동시킨다.
            if stack:
                now = stack[-1]
            # 빈 스택이 아닌경우 반복문을 탈출한다.
            else :
                break
    return

print(dfs(1,6))