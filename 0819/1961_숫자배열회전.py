import sys
sys.stdin = open("숫자배열.txt")

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    table = []
    for _ in range(n):
        table.append(input().split())

    # 각 숫자는 int형이 아닌, string형으로 넣어서 나중에 더할 수 있게끔 만들었다.
    ans = [[] for __ in range(n)]

    # 시계방향으로 90도 회전
    for i in range(0, n):
        num = ""
        for j in range(n-1, -1, -1):
            num += table[j][i]
        ans[i].append(num)

    # 시계방향으로 180도 회전
    for i in range(n-1,-1,-1):
        num = ""
        for j in range(n-1,-1,-1):
            num += table[i][j]
        ans[n-1-i].append(num)

    # 시계방향으로 270도 회전
    for i in range(n-1,-1,-1):
        num = ""
        for j in range(n):
            num += table[j][i]
        ans[n-1-i].append(num)
    print(f"#{tc}")
    for k in range(n):
        for m in range(3):
            print(ans[k][m], end=" ")
        print()
