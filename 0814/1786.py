t = input()
p = input()

def kmp(t, p):
    N = len(t)
    M = len(p)
    lps = [0] * (M+1)
    # preprocessing, 전처리
    # 패턴 중에 중복되는 부분을 찾는다.
    # 일치했었다 라는 정보를 이용해 중복되는 부분을 통해 어디까지 건너뛸지 계산하기 위함
    j = 0 # 일치한 개수== 비교할 패턴 위치
    lps[0] = -1
    for i in range(1, M):
        lps[i] = j          # p[i]이전에 일치한 개수
        if p[i] == p[j]:
            j += 1
        else:
            j = 0
    lps[M] = j

    cnt = 0
    empty_list = []
    # search
    i = 0   # 비교할 텍스트 위치
    j = 0   # 비교할 패턴 위치
    while i < N and j <= M:
        if j==-1 or t[i]== p[j]:     # 첫글자가 불일치했거나, 일치하면 일치하지 않을때까지 쭉
            i += 1
            j += 1
        else:               # 일치하지 않는 순간 j는 돌아갈 위치를 찾아서 간다.
            j = lps[j]
        if j==M:    # 패턴을 찾을 경우 ( 비교할 패턴 위치가 돌아가지 않고 무사히 마지막위치까지 왔다!! )
            cnt += 1
            empty_list.append(i - M + 1)  # 패턴의 인덱스 출력
            j = lps[j]

    return cnt, empty_list


answer_count = kmp(t, p)[0]
answer_list = kmp(t, p)[1]
print(answer_count)
if len(answer_list) == 0:
    print(0)
else :
    for i in answer_list:
        print(i, end=" ")
