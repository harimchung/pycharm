import sys
sys.stdin = open('백만장자.txt')

# 제일 높은 가격을 출력하는 함수를 만든다.
# 변수로는 리스트의 길이와 가격 리스트를 받는다.
def largest(list):
    # 가격 리스트에서 가장 가격이 높은 날의 가격과 그때의 index 값을 찾는다.
    max_price = max(list)
    max_index = list.index(max_price)
    n = len(list)
    # 이익을 출력할 변수를 새로 만든다.
    profit = 0

    # 제일 비싼날이 마지막 날이라면, 이익을 출력하고 끝낸다.
    # 그렇지 않다면 제일 비싼 날 전날까지 하나씩 사서
    # 제일 비싼 날에 판다
    for i in range(max_index):
        profit -= list[i]
    profit += max_price*max_index

    # 만약 제일 비싼 날이 마지막 날이라면,팔고 끝낸다.
    if max_index == n-1:
        return profit
    # 그렇지 않다면, 남은 날들에 대해서 다시 이익을 구한다.
    else:
        return profit + largest(list[max_index+1::])


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    prices = list(map(int, input().split()))
    print(f"#{tc} {largest(prices)}")