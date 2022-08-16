import sys
sys.stdin = open('회문.txt')

# 총 10개의 테스트케이스가 주어진다.
# 이거 야매..인데 답에서 제일 큰게 21이라
# 제일 큰 문자의 길이를 21로 제한하고 시작했다.

# 일단 이렇게 풀어보고 다음으로는 다르게 풀어보려고 한다.

# 총 10개의 테스트케이스가 주어지기 때문에,
# 아래의 과정을 10번 반복한다.
for _ in range(10):
    tc = int(input())
    # 100x100을 담는 words list를 생성한다.
    words = [list(c for c in input()) for _ in range (100)]

    max = 0
    # 가로 길이에서 제일 긴 것 찾기
    for k in range (2,100):
        for i in range(100):
            for j in range(100-k+1):
                word_row = ""
                for m in range(k):
                    word_row += words[i][j+m]
                if word_row == word_row[::-1]:
                    if k > max:
                        max = k

    # 세로 길이에서 제일 긴 것 찾기
    for k in range(2, 100):
        for i in range(100):
            for j in range(100 - k + 1):
                word_row = ""
                for m in range(k):
                    word_row += words[j + m][i]
                if word_row == word_row[::-1]:
                    if k > max:
                        max = k
    print(f"#{tc} {max}")