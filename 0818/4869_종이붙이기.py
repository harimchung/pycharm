
T = int(input())
for tc in range(1, T+1):
    # 테스트 케이스 별로 한 변의 길이가 주어진다.
    n = int(input())
    m = n // 10
    # mix는 한 변의 길이가 주어졌을 때 만들 수 있는 조합을 의미한다.
    mix = [0,1,3]

    for i in range(3,m+1):
        a = mix[i-2]*2 + mix[i-1]
        mix.append(a)
    print(f"#{tc} {mix[m]}")