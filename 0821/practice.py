board = [list(map(int, input().split())) for _ in range(9)]
for i in range(0, 9, 3):
    for j in range(0, 9, 3):
        print(board[i][j])