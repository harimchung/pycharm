di = [-1, 1, 0, 0]  # 상 하 좌 우
dj = [0, 0, -1, 1]  # 상 하 좌 우


def miro(start, end):
    visited = [[0] * n for _ in range(n)]
    visited[start[0]][start[1]] = 1
    q = []
    q.append(start)
    result = 0


    while q:
        result += 1
        cnt = len(q)
        while cnt:
            a = q.pop(0)
            ni = a[0]
            nj = a[1]
            for i in range(4):
                ri = ni + di[i]
                rj = nj + dj[i]
                if 0 <= ri < n and 0 <= rj < n and arr[ri][rj] != 1 and visited[ri][rj] != 1:
                    visited[ri][rj] = 1
                    q.append([ri, rj])
                if end[0] == ri and end[1] == rj:
                    return result - 1
            cnt -= 1
    return 0

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = [list(input()) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if int(arr[i][j]) == 2:
            start = [i, j]  # [4, 3]
        elif int(arr[i][j]) == 3:
            end = [i, j]  # [0, 1]

print(f'#{tc} {miro(start, end)}')
