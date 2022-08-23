# 1918 후위표기식

stack = []
icp = {"+":1, "-":1, "*":2, "/":2, "(":3}

words = input()
postfix = ""
for word in words:
    # 만약 피연산자이면 postfix에 추가하고
    if word.isalpha():
        postfix += word

    # 연산자이면 stack에 push 한다.
    else:
        # 만약 stack이 비었다면 push 한다.
        if not stack:
            stack.append(word)

        # stack이 비지 않았다면,
        else:
            # 만약 닫는 괄호가 들어오면, 여는 괄호가 올 때까지 pop한다.
            if word ==")":
                while stack[top] == "(":
                    postfix += stack.pop()
                    top = stack[-1]
            # 다른 문자가 들어온다면,
            else:
                # stack의 top보다 우선순위가 크면 push 한다.
                top = stack[-1]
                if icp(top) < icp(word):
                        stack.append(word)

                elif icp(top) >= icp(word):
                    while len(stack)!=0 and icp(top) < icp(word):




