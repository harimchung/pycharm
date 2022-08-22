prior = {"+":1,  "*":2}

for tc in range(1,11):
    # 문자열의 길이
    n = int(input())
    infix = input()

    # 후위 표기식으로 만들기
    postfix = ""
    stack = [0]*n
    top = -1
    for i in range (n):
        if '0' <= infix[i] <= '9':
            postfix += infix[i]

        else:
            if top > -1 and prior[stack[top]] >= prior[infix[i]]:
                postfix += stack[top]
                top -= 1

            top += 1
            stack[top] = infix[i]

    while top > -1:
        postfix += stack[top]
        top -= 1

    # 후위표기식으로 만든 계산식 계산하기
    calculate = []

    for j in range(n):
        if '0' <= postfix[j] <= '9':
            calculate.append(int(postfix[j]))

        else:
            a = calculate.pop()
            b = calculate.pop()
            if postfix[j] == "+":
                calculate.append(b+a)
            elif postfix[j] == "*":
                calculate.append(b*a)

    ans = calculate.pop()

    print(f"#{tc} {ans}")