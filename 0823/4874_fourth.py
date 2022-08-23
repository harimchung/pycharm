T = int(input())
for tc in range(1, T+1):
    stack = []

    postfix = list(input().split())
    n = len(postfix)

    result = 0
    i = 0

    while postfix[i] != ".":
        if postfix[i] != "+" and postfix[i] != "*" and postfix[i] != "/" and postfix[i] != "-":
            stack.append(postfix[i])
            i += 1

        else:
            if len(stack) > 1 :
                a = int(stack.pop())
                b = int(stack.pop())

                if postfix[i] == "+":
                    result = a + b
                elif postfix[i] == "*":
                    result = a * b
                elif postfix[i] == "/":
                    result = b // a
                elif postfix[i] == "-":
                    result = b - a

                stack.append(result)
                i += 1

            else :
                stack.pop()
                ans = "error"
                break

    if len(stack) == 1 :
        ans = stack.pop()
    elif len(stack) > 1:
        ans = "error"

    print(f"#{tc} {ans}")