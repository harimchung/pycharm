di = [1, -1, 0, 0]
dj = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    max_v = 0

    for i in range(n):
        for j in range(n):
            cnt1 = arr[i][j]
            for k in range(4):
                for z in range(1, m):
                    ni, nj = i + di[k]*z, j + dj[k]*z
                    if 0<= ni < n and 0<= nj < n:
                        cnt1 += arr[ni][nj]
            if max_v < cnt1:
                max_v = cnt1

            cnt2 = arr[i][j]
            for di1, dj2 in [[1,1],[1,-1],[-1,-1],[-1,1]]:
                for z in range(1,m):
                    ni, nj = i+di1*z, j+dj2*z
                    if 0<= ni<n and 0<=nj<n:
                        cnt2 += arr[ni][nj]
                if max_v < cnt2:
                    max_v = cnt2
    print(f"#{tc} {max_v}")
