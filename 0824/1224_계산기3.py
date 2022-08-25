icp = {"+":1, "*":2, "(":3}
isp = {"+":1, "*":2, "(":0}

def get_postfix(infix, n):
    postfix = "" # 결과로 나올 후위표기식
    stack = []

    for i in range(n): # 중위표기식 하나씩 떼서 확인
        if "0" <= infix[i] <= "9":
            postfix += infix[i]
        else:
            if infix[i] == ")":
                while stack:
                    char = stack.pop()
                    if char == "(":
                        break
                    postfix += char
            else:
                while stack and isp[stack[-1]] >= icp[infix[i]]:
                    postfix += stack.pop()
                stack.append(infix[i])
    while stack:
        postfix += stack.pop()
    return postfix


def get_result(postfix):
    stack = []
    for c in postfix:
        if "0"<= c <= "9":
            stack.append(int(c))
        else:
            right = stack.pop()
            left = stack.left()

            if c=="+":
                result = left+right
            elif c == "*":
                result = left*right

            stack.append*result
    return stack.pop()

T = 10
for tc in range(1, T+1):
    n = int(input())
    exp = input()

    postfix = get_postfix(exp,n)
    answer = get_result(postfix)

    print(f"#{tc} {answer}")