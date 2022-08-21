T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    num = [list(map(int, input().split())) for _ in range(n)]
    max_num = 0

    # 가로에서 탐색
    for i in range(n):
        a = 0
        for j in range(m):
            if num[i][j] == 1:
                a += 1
            else :
                if a > max_num:
                    max_num = a
                a = 0

        if a > max_num:
            max_num = a
        # 연속된 1의 개수를 저장할 변수를 초기화 한다.


    # 세로에서 탐색
    for j in range(m):
        a = 0
        for i in range(n):
            if num[i][j] == 1:
                a += 1
            else:
                if a > max_num:
                    max_num = a
                a = 0

        if a > max_num:
            max_num = a
    print(f"#{tc} {max_num}")

# 1
# 3 5
# 0 1 0
# 0 1 0
# 0 1 0
# 1 1 1
# 1 1 0