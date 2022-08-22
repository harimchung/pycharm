T = int(input())
for tc in range(1, T+1):
    board = [list(map(int, input().split())) for _ in range(9)]
    ans = 1
    # 가로 검증
    for i in range(9):
        a = 0
        for j in range(9):
            a += board[i][j]
        if a != 45:
            ans = 0
    # 세로검증
    for j in range(9):
        a = 0
        for i in range(9):
            a += board[i][j]
        if a != 45:
            ans = 0
    # 3x3칸 검증
    for i in range(0, 9, 3):
        for j in range(0,9,3):
            a = 0
            for k in range(3):
                for l in range(3):
                    a += board[i+k][j+l]
            if a!= 45:
                ans = 0

    print(f"#{tc} {ans}")