T = int(input())
for tc in range(1, T+1):
    words = [c for c in input()]
    n = len(words)
    stack = []
    cnt = 0
    for i in range(n):
        if words[i] == "(":
            stack.append(words[i])
        else :
            if words[i-1] != "(":
                stack.pop()
                cnt += 1
            else:
                stack.pop()
                n = len(stack)
                cnt += n
    print(f"#{tc} {cnt}")
# 1
# (((()(()()))(())()))(()())