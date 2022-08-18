# 첫 줄에 테스트케이스의 개수가 주어진다.
T = int(input())
# 테스트 케이스의 개수만큼 아래를 반복한다.
for tc in range(1,T+1):
    # 문자열을 입력받는다.
    words = input()
    n = len(words)
    stack = []
    # 입력 받은 문자열에 대해서, 첫번째 문자열은 stack 에 추가한다.
    stack.append(words[0])

    # 인덱스는 words의 첫번째부터 마지막 문자까지 돌면서 다음을 수행한다.
    for i in range(1, n):
        # 만약 stack이 비어있다면 무조건 append 하세요.
        if not stack:
            stack.append(words[i])

        # 그렇지 않다면 비교합시다.
        else:
            # 만약 다음에 들어오는 문자가 top과 같다면
            if words[i] == stack[-1]:
                # stack에서 문자를 뽑으세요.
                stack.pop()
            # 문자가 다르다면, stack에 append 하세요.
            else :
                stack.append(words[i])

    # 반복문을 다 돌고 나서 stack 의 길이를 출력하세요.
    a = len(stack)
    print(f"#{tc} {a}")


