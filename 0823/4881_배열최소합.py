def backtracking(r, sum):
    # 함수안에서 전역변수를 사용하고 싶은 경우,
    # 1. 수정하지 않고 읽기만 한다 => 파이썬의 이름찾기 공식에 따라서
    # 2. 수정해야 한다. => 쓰던대로 쓰면, 지역변수가 되어버린다!
    #       global 키워드로 전역변수를 사용한다고 꼭 선언해야 한다!
    # 전역변수로 쓰지 말고 함수의 파라미터로 다 가지고 다니는 방법

    global ans
    global col

    if r == n: # 다 고르고나면 r이 2차원 배열의 크기만큼 되어있다. => 중단조건
        if ans > sum:
            ans = sum # 최소합 비교해서 저장
        return

    # 내가 알고 있는 최소 합보다 현재 합이 더 커버리면 더이상 진행할 필요가 없다. (가망이 없다.)
    if sum > ans:
        return

    # 열에 대해서 순회
    for c in range(n):
        # 이전에 현재 열에 있는 숫자를 고른 적이 있는지 검사
        if col[c] == 0:
            # 전에 골랐던 열이랑 안겹치면 골랐다고 체크
            col[c] = 1
            # 고른 수와 합을 구하고 다음 행으로 이동 (재귀)
            backtracking(r+1, sum+arr[r][c])
            # 함수가 끝나고 나면 다시 돌아옴, 이번 열에 골랐다고 체크한 것을 다시 원복
            col[c] = 0

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    col = [0] * n
    ans = 10*n
    backtracking(0, 0)

    print(f"#{tc} {ans}")