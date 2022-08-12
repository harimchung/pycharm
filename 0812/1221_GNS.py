# GNS
# 처음에는 테스트케이스의 번호가 주어진다.
T = int(input())

for tc in range(1,T+1):
    # #1 7041 의 형태로 번호와 문자열의 길이를 입력받는다.
    number, n = input().split()
    n = int(n)
    # 정렬되기 전 문자열을 s로 입력받는다.
    s = input()

    # 문자열에서 3칸씩 건너뛰면서 어떤 숫자가 나왔는지 숫자를 센다
    # 각 숫자를 구별하려면, 첫 두 문자만 비교하면 된다.
    for i in range (0, n+1, 3):
        for j in range(i, i+2):
            print(s[j])
    print(f"#{number}")