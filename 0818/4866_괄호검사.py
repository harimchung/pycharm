T = int(input())
for tc in range(1, T+1):
    stack = []
    words = input()
    answer = 1
    for word in words:
        # 만약 여는 괄호가 나오면 stack 에 넣는다.
        if word == '{' or word == '(':
            stack.append(word)

        elif word == '}' or word == ')' :
            # 닫는 괄호가 나오면 stack 안에 문자가 있을떄, stack에서 맨마지막 값을 꺼낸다.
            # 꺼내서 보았을 때, 짝이 맞지 않으면 answer값을 바꾼다.
            if stack:
                a = stack.pop(-1)
                if word == "}" and a != "{":
                    answer = 0
                if word == ")" and a!= "(":
                    answer = 0
            # stack안이 빈 값인 경우 answer == 0으로 만든다.
            else :
                answer = 0

    # 반복문을 다 돌고나서 stack에 괄호가 남아있다면,
    # 즉 짝의 개수가 맞지 않는다면 ansewr을 바꾼다.
    if stack:
        answer = 0

    print(f"#{tc} {answer}")