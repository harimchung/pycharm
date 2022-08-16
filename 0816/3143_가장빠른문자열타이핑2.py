T = int(input())
for tc in range(1,T+1):
    a, b = input().split()

    typing = 0

    a_len = len(a)
    b_len = len(b)

    idx = 0 # a의 인덱스 (처음부터 시작)
    while idx < a_len - b_len +1 :
        # 패턴을 비교할 수 있을 만큼 비교 (텍스트 길이 - 패턴 길이)
        # 텍스트를 단어 b의 길이 만큼 잘라서 패턴과 비교를 한다.
        # 같으면 개수를 1 증가
        # 인덱스를 b의 길이만큼 뒤로 이동시킨다.

        sub = ""
        for i in range(b_len):
            sub += a[idx+i]
        if sub == b:
            typing += 1
            idx += b_len
        else :
            # 다르면 한 칸만 뒤로 가서 비교를 이어 간다.
            typing += 1
            idx += 1
        # 남은 문자를 처리 (텍스트의 마지막 부분, 패턴 길이보다 짧음)
        while idx < a_len :
            typing += 1
            idx += 1
    print(f"#{tc} {typing}")

