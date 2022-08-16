import sys
sys.stdin = open('백만장자.txt')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    prices = list(map(int, input().split()))
    # 살지 말지를 결정하는 buy or not 이라는 리스트를 만들었다.
    buy_or_not = [0]*n

    # 미래를 알고 주식을 하는 것과 똑같다.
    # 가장 끝날로 가서 나보다 싸면 사고, 나보다 비싸면 안산다.
    # 구매할 경우 list의 값을 1로 바꾼다.
    for i in range(n-1,-1,-1):
        for j in range(i-1,-1,-1):
            if prices[i] > prices[j]:
                buy_or_not[j] = 1
            else:
                break
    # 완성된 buy_or_not에서 값이 1이면 구매하고, 처음으로 0을 만나게 되는 지점에서 팔면 된다.
    profit = 0 # 총 이익 (판매가격-구매가격)
    buy = 0 # 구매가격
    count = 0 # 구매한 횟수
    for j in range(n):
        if buy_or_not[j] == 1:
            buy -= prices[j]
            count += 1
        else :
            # 이익을 먼저 계산하고 ( 이익 + 판매한 가격 - 구매한가격)
            profit = profit + buy + prices[j]*count
            # buy 값과 count 값을 다시 0으로 돌린다.
            buy = 0
            count = 0

    print(f"#{tc} {profit}")
