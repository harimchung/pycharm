T = 10

icp = {"+":1, "*":2}

for tc in range(1, T+1):
    n = int(input())

    exp = input()
    postfix = ""

    stack = []

    for i in range(n):
        # 피연산자인 경우,
        if "0" <= exp[i] <= "9":
            # 그냥 결과 문자열에 이어붙이기
            postfix += exp[i]

        # 연산자인 경우,
        else:
            # top을 확인해서, 자신보다 같거나 높은 우선순위를 가진 연산자가 있으면 꺼낸다.
            if stack and icp[stack[-1]] >= icp[exp[i]]:
                postfix += stack.pop()

            stack.append(exp[i])

    # 스택에 남아있는 연산자는 뒤에 붙이기
    while stack:
        postfix += stack.pop()

    # 후위표기식 계산
    result = 0
    stack = []
    k = len(postfix)
    for i in range(k):
        # 피연산자가 나오면 stack에 추가하고
        if "0"<= postfix[i] <= "9":
            stack.apped(postfix[i])
        # 연산자가 나오면 계산 (앞에 두 피연산자를 선택)
        else :
            right = int(stack.pop())
            left = int(stack.pop())

            if postfix[i] == "+":
                result = right + left
            else :
                result = right * left

            stack.append(result) # 계산하고 그 결과를 스택에 다시 넣어주기 (차후를 위해)
    print(f"#{tc} {result}")