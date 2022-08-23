T = int(input())
for tc in range(1, T+1):
    num = list(input().split())
    n = len(num)

    stack = [0] * 256
    ans = 0
    top = -1
    for i in range(n-1):
        # 만약 num이 숫자라면, stack 에 넣습니다.
        if num[i] != ""
        # 연산자라면, 두개의 숫자를 꺼내서 연산 후 다시 집어 넣습니다.
            #
        #
