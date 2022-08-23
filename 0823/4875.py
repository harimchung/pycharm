def dfs(i, j, N):
    stack = []
    di = [-1, 1, 0, 1]
    dj = [0, 0, -1, 1]

    while True:

        if arr[i][j] == 3:
            return 1

        arr[i][j] = 1

        for d in range(4):
            ni = di[d] + i
            nj = dj[d] + j

            if 0<= ni < N and 0 <= nj < N and arr[ni][nj] == 0:
                stack.append((ni, nj))
                i, j = ni, nj
                break

        else:
            if stack:
                i, j = stack.pop()

            else:
                break

        return 0


T = int(input())

for tc in range(1, T+1):
    n = int(input())

    arr = [list(map(int, input())) for _ in range(n)]

    si = sj = 0

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                si = i
                sj = j

    print(f"{tc} {dfs(si, sj, n)}")