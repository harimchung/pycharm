


# 8 10
# 1 2
# 1 3
# 2 4
# 2 5
# 3 6
# 3 7
# 4 8
# 5 8
# 6 8
# 7 8

# def dfs(s,V):
    # 현재 위치는 s, 노드의 개수는 V개
    # 방문했는지 여부를 기록할 리스트를 만든다.
    # 마지막으로 방문한 위치를 기록할 stack을 만든다.

    # 초기 위치를 방문했다고 기록한다.

    # 돌아갈 곳이 없을 때까지 반복한다.
        # 현재 위치에 인접한 리스트를 돌면서
            # 인접하면서 아직 방문하지 않은 곳이 있다면.
            # 현재 위치를 stack에 넣는다.
            # 인접한 곳으로 이동한다.
            # 이동한 후에는 break를 통해 반복문을 빠져나온다.

        # for문을 다 돌고, 더이상 갈 곳이 없다면
            # stack이 비어있지 않다면,
                # 현재 위치를 stack의 맨 마지막 곳으로 이동시킨다.
            # stack이 비어서 더이상 갈 곳이 없다면.
                # while문을 탈출해서 나온다.
# def dfs1(s,V):
#     # 현재 위치는 s, 노드의 개수는 V개
#     # 방문했는지 여부를 기록할 리스트를 만든다.
#     visited = [0]*(V+1)                                      # 인덱스의 편의를 위해서 V+1개를 만든다.
#                                                              # 0번 인덱스는 사용하지 않는다.
#                                                             # 방문하지 않으면 0, 방문하면 1로 표시하려고 한다.
#     # 마지막으로 방문한 위치를 기록할 stack을 만든다.
#     stack = []
#     # 초기 위치를 방문했다고 기록한다.
#     visited[s] = 1
#     print(s)
#     # 돌아갈 곳이 없을 때까지 반복한다.
#     while True:
#         # 현재 위치에 인접한 리스트를 돌면서
#         for i in adj[s]:
#             # 인접하면서 아직 방문하지 않은 곳이 있다면.
#             if visited[i] == 0:
#                 # 현재 위치를 stack에 넣는다.
#                 stack.append(s)
#                 # 인접한 곳으로 이동한다.
#                 s = i
#                 visited[s] = 1
#                 print(s)                                          # 이동했으면 출력한다.
#                 # 이동한 후에는 break를 통해 for문을 빠져나온다.
#                 break
#             # 이제 바뀐 s에대해서 다시 반복문이 돌아간다.
#
#         # for문을 다 돌고, 더이상 갈 곳이 없다면
#         else:
#             # stack이 비어있지 않다면,
#             if stack:                                           # 이 표현은 stack 안에 원소가 있으면 True가 나와서 실행된다.
#                 # 현재 위치를 stack의 맨 마지막 곳으로 이동시킨다.
#                 s = stack[-1]
#             # stack이 비어서 더이상 갈 곳이 없다면.
#             else:
#                 # while문을 탈출해서 나온다.
#
#                 break
# dfs1(1,8)

# def dfs(s):
#     # 재귀함수를 사용하면, 맨 처음 위치를 입력받는다.
#     print(s)
#     visited[s] = 1
#     for i in adj[s]:
#         if visited[i] == 0:
#             dfs(i)
#
# V, E = map(int, input().split())
# adj = [[] for _ in range(V+1)]
#
# for _ in range(E):
#     a, b = map(int, input().split()) #a는 adj안에 있는 리스트의 인덱스, b는 노드 번호이다.
#     adj[a].append(b)
#     adj[b].append(a)                 # 만약 일방통행이라면 이 코드를 삭제하면 된다.
#
# visited = [0]*(V+1)
# dfs(1)

# 재귀함수를 사용하여 dfs
def dfs4(s):
    print(s)
    visited[s] = 1
    for i in range(V+1):
        if adj[s][i] ==1 and visited[i] == 0:
            dfs4(i)

V, E = map(int, input().split())
adj = [[0]*(V+1) for _ in range(V+1)]

for _ in range(E):
    a, b = map(int, input().split())
    adj[a][b] = 1
    adj[b][a] = 1
visited = [0]*(V+1)

dfs4(1)
#
#
# def dfs2(s,V):
#     # 현재 위치는 s, 노드의 개수는 V개
#     # 방문했는지 여부를 기록할 리스트를 만든다.
#     visited = [0] * (V+1)
#     # 마지막으로 방문한 위치를 기록할 stack을 만든다.
#     stack = []
#     # 초기 위치를 방문했다고 기록한다.
#     visited[s] = 1
#     print(s)
#     # 돌아갈 곳이 없을 때까지 반복한다.
#     while True:
#         # 현재 위치에 인접한 리스트를 돌면서
#         for i in range(V+1):
#             # 인접하면서 아직 방문하지 않은 곳이 있다면.
#             if adj[s][i] == 1 and visited[i] == 0:
#                 # 현재 위치를 stack에 넣는다.
#                 stack.append(s)
#                 # 인접한 곳으로 이동한다.
#                 s = i
#                 visited[i] = 1
#                 print(s)
#                 # 이동한 후에는 break를 통해 반복문을 빠져나온다.
#                 break
#         # for문을 다 돌고, 더이상 갈 곳이 없다면
#         else:
#             # stack이 비어있지 않다면,
#             if stack:
#                 # 현재 위치를 stack의 맨 마지막 곳으로 이동시킨다.
#                 s = stack.pop()
#             # stack이 비어서 더이상 갈 곳이 없다면.
#             else:
#                 # while문을 탈출해서 나온다.
#                 break
#
# dfs2(1,8)

