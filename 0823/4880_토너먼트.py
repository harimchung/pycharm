# 가위바위 보에 대한 함수를 만든다.
def rsp(a, b):
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
    m = n // 2
    # 다음으로 들어오는 숫자들에 대해서 리스트로 받는다.
    num = list(map(int, input().split()))
    stack1 = []
    stack2 = []

    for i in range(0, m):
        # 만약 스택이 비어있다면, push 한다.
        if not stack1:
            stack1.append(i)
        # 스택 안에 값이 있다면, 가위바위 보 함수를 한다.
        else :
            a = stack1.pop()
            b = i
            # 이 때, push 하는 값은 인덱스 번호이다.
            stack1.append(rsp(a, b))

    for j in range(m, n):
        # 만약 스택이 비어있다면, push 한다.
        if not stack2:
            stack2.append(j)
        # 스택 안에 값이 있다면, 가위바위 보 함수를 한다.
        else:
            a = stack2.pop()
            b = j
            # 이 때, push 하는 값은 인덱스 번호이다.
            stack2.append(rsp(a, b))

    ans = rsp(stack1[0], stack2[0])

    print(f"#{tc} {ans+1}")

