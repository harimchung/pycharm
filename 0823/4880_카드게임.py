# i, j : i번째 학생부터 j번째 학생까지를 말한다.
def tournament(i,j):
    # 분할
    if i == j:
        return i
    else:
        left = tournament(i, (i+j)// 2)
        right = tournament((i+j)//2+1, j)
        return winner(left, right) #left와 right 중 승자를 구해서 리턴

# 승자의 인덱스를 리턴한다.
def winner(a, b):
    if num[a] == 1 and num[b] == 3:
        return a

    if num[a] == 3 and num[b] == 1:
        return b

    else:
        if num[a] >= num[b]:
            return a
        return b

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    # 다음으로 들어오는 숫자들에 대해서 리스트로 받는다.
    num = list(map(int, input().split()))
    ans = tournament(0, n-1)

    print(f"#{tc} {ans+1}")
