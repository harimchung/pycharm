# 괄호가 있는 후위계산식 만들기

icp = {"+":1, "*":2, "(":3}
isp = {"+":1, "*":2, "(":0}


for tc in range(1, 11):
    n = int(input())
    words = input()
    stack = []
    postfix = ""


    # 괄호가 있는 중위연산식을 후위계산식으로 만들기
    for word in words:
        # 만약 피연산자이면 postfix에 추가하고
        if word.isdecimal():
            postfix += word

        # 연산자인 경우,
        else:
            # 만약 stack이 비었다면 push 한다.
            if not stack:
                stack.append(word)

            # stack이 비지 않았다면,
            else:
                # 만약 닫는 괄호가 들어오면, 여는 괄호가 올 때까지 pop한다.
                if word == ")":
                    top = stack[-1]
                    while top != "(":
                        postfix += stack.pop()
                        if stack:
                            top = stack[-1]
                    # 여는 괄호를 없애준다.
                    stack.pop()

                # 다른 문자가 들어온다면,
                else:
                    # stack의 top보다 우선순위보다 들어오는 단어의 우선순위가 크면 push 한다.
                    top = stack[-1]
                    if isp[top] < icp[word]:
                        stack.append(word)

                    # stack의 top의 우선순위보다 들어오는 우선순위가 같거나 낮으면,
                    else:
                        # 우선순위가 낮은게 나올 때까지 팝한다.
                        while len(stack) != 0 and isp[top] >= icp[word]:
                            postfix += stack.pop()
                            if stack:
                                top = stack[-1]
                        # 다 끝난 후에 append 해준다.
                        stack.append(word)

    # 단어를 다 순회하고 나서 stack에 남아있는 문자를 다 더해준다.
    while stack:
        postfix += stack.pop()

    # 후위계산식을 다시 계산하는 과정
    l = len(postfix)
    stack2 = []
    result = 0

    for i in range(l):
        # 숫자이면 stack에 넣고, 그렇지 않으면 pop해서 계산한다.
        if "0" <= postfix[i] <= "9":
            stack2.append(postfix[i])
        else :
            right = int(stack2.pop())
            left = int(stack2.pop())

            if postfix[i] == "+":
                result = left + right
            elif postfix[i] == "*":
                result = left * right

            stack2.append(result)

    ans = stack2.pop()
    print(f"#{tc} {ans}")
