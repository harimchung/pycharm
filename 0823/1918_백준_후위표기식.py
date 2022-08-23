
icp = {"+":1, "-":1, "*":2, "/":2, "(":3}
isp = {"+":1, "-":1, "*":2, "/":2, "(":0}


postfix = ""
top = -1

words = input()
n = len(words)
stack = [0]*n

for i in range(n):
    # 만약 문자이면 postfix에 더한다
    if words[i].isalpha():
        postfix += words[i]

    # 연산자이면
    else:
        # top = -1 이면(즉, 스택이 비어있으면)
        if top == -1:
            # stack에 push 한다.
            top += 1
            stack[top] = words[i]
        # 그렇지 않으면 (즉, 스택이 비어있지 않으면)
        else:
            # 닫는 괄호가 들어오면, 여는괄호가 나올때까지 pop한다.
            if words[i] == ")":
                while stack[top] != "(":
                    postfix += stack[top]
                    top -= 1
                # "(" 을 pop한다. (즉 top을 하나 낮춘다.)
                top -= 1
            else:
                # icp(stack(top)) > isp(i)을 비교한다.
                if isp[stack[top]] < icp[words[i]]:
                    # stack에 push 한다.
                    top += 1
                    stack[top] = words[i]
                # icp(top) <= isp(i) 라면,
                else:
                    # top = -1 이거나 icp(top) < isp(i)가 될때까지 pop 한다.
                    while top != -1 and isp[stack[top]] >= icp[words[i]]:
                        postfix += stack[top]
                        top -= 1
                    # push 한다.
                    top += 1
                    stack[top] = words[i]
# 반복문을 다 돌고 stack에 남아있는 것이 있다면
# postfix에 붙인다.
while top != -1:
    postfix += stack[top]
    top -= 1


print(postfix)