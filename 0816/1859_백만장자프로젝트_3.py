import sys
sys.stdin = open('백만장자.txt')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    prices = list(map(int, input().split()))

    # 무엇보다.. 가장 중요한 것은 max 값이다.
    # 뒤에서부터 찾는 max값이 가장 중요함!

    profit = 0  # 총 이익 (판매가격-구매가격)
    buy = 0  # 구매가격
    count = 0  # 구매한 횟수

    max_v = n-1
    for i in range (max_v-1,-1,-1):

        # 만약에 이전의 값보다 더 큰 (비싼) 값이 나오면 max 값을 이동시킨다.
        if prices[max_v] < prices[i]:
            max_v = i
        # 그렇지 않다면, 구매가격에서 값을 빼고
        # 이익에는 최대가격을 더한다.
        buy -= prices[i]
        profit += prices[max_v]
        total = buy+profit

    print(f"#{tc} {total}")
