di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

# dfs 로 풀이하기
def dfs(g, si, sj):
    stack = []
    # visited를 따로 만들지 않고, 이미 지나온 칸을 칠하는 방식으로 진행
    stack.append((si,sj))
    g[si][sj] = 1

    while stack:
        i, j = stack.pop()
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if 0<= ni < 16 and 0<= nj <16 and g[ni][nj] != 1:
                if g[ni][nj] == 3:
                    return 1
                stack.append((ni,nj))
                g[ni][nj] = 1
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

    print(f"#{tc} {dfs(arr, si,sj)}")