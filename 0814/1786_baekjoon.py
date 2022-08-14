t = input()
p = input()

def index_in_pattern(pattern):
    # pattern은 문자열(string) 이다.
    n = len(pattern)
    box = [0]*n
    i = 0
    j = 1
    # j는 pattern을 순회하면서 돌 index 이다.
    while j < n :
        if 0<= j <n and pattern[i] == pattern[j]:
            box[j] = i + 1
            i += 1
            j += 1
        elif 0<= j <n and pattern[i] != pattern[j]:
            i = box[i-1]
            if i == 0:
                j += 1

    return box

pattern_box = index_in_pattern(p)

def find_pattern(text,pattern):
    n = len(text)
    m = len(pattern)

    i = 0 # 텍스트를 순회할 인덱스를 i라고 한다.
    j = 0 # 패턴을 순회할 인덱스를 j 라고 한다.

    cnt = 0
    empty_list = []
    # text의 인덱스가 끝까지 돌때까지 반복한다.
    while i < n and j < m:
        if text[i] == pattern[j]:
            j += 1
            i += 1
            # 텍스트의 인덱스 값과, 패턴의 인덱스 값이 일치하면 값을 1씩 증가시킨다.
        if j == 0 and text[i] != pattern[j]:
            i += 1

        if j == m:
            cnt += 1
            empty_list.append(i-m+1)
            j = 0
            i += 1

        elif text[i] != pattern[j]:
            # 만약 불일치 하는 지점이 발생했다면, j는 위에서 만들어둔 box의 [j-1]번째 값으로 돌아간다.
            j = pattern_box[j-1]
            # 만약 j가 0인데, 불일치 하는 지점이라면, i를 1 증가시켜 다음 i값과 j값을 비교한다.

    return cnt, empty_list

try:
    answer_count = find_pattern(t,p)[0]
    answer_list = find_pattern(t,p)[1]
    print(answer_count)
    for i in answer_list:
        print(i, end=" ")
except:
    print(0)
    print(0)