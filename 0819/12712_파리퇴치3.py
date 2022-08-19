T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())

    board = [list(map(int, input().split())) for _ in range(n)]
    max_fly = 0
    # + 모양으로 분사하기
    for i in range(n):
        for j in range(n):
            # 시작점 구하기, 파리의 개수 초기화하기
            x, y = j, i
            fly = 0
            # 반복문을 돌면서 상/하/좌/우에 갈 수 있는 만큼 가고 fly에 더하기
            for k in range(1,m):
                if 0<= x-k <n:
                    fly += board[y][x-k]
                if 0<= x+k <n:
                    fly += board[y][x+k]
                if 0<= y-k <n:
                    fly += board[y-k][x]
                if 0<= y+k <n:
                    fly += board[y+k][x]
            fly += board[y][x]
            if fly > max_fly:
                max_fly = fly

    # x 모양으로 분사하기
    for i in range(n):
        for j in range(n):
            # 시작점 구하기, 파리의 개수 초기화하기
            x, y = j, i
            fly = 0
            # 반복문을 돌면서 상/하/좌/우에 갈 수 있는 만큼 가고 fly에 더하기
            for k in range(1,m):
                if 0<= x-k <n and 0<= y-k <n:
                    fly += board[y-k][x-k]
                if 0<= x+k <n and 0<= y+k <n:
                    fly += board[y+k][x+k]
                if 0<= x+k <n and 0<= y-k <n:
                    fly += board[y-k][x+k]
                if 0<= x-k <n and 0<= y+k <n:
                    fly += board[y+k][x-k]
            fly += board[y][x]
            if fly > max_fly:
                max_fly = fly

    print(f"#{tc} {max_fly}")