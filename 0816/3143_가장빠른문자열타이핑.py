T = int(input())
for tc in range(1,T+1):
    a, b = input().split()
    # 예를 들어 banana bana 가 입력되면
    # a = banana, b = bana 로 따로 저장된다. (문자열로)

    cnt = 0
    n = len(a)
    m = len(b)

    i = 0 # 문자열 a를 탐색할 인덱스
    j = 0 # 문자열 b를 탐색할 인덱스
    cnt = 0

    while i < n and j < m:
        if a[i] != b[j]:
            i = i-j
            j = -1
        i += 1
        j += 1
        if j == m:
            cnt += 1
            j = 0

    total = n-(cnt*m) + cnt
    print(f"#{tc} {total}")

