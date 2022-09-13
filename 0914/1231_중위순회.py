def inorder(i):
    if left[i]:
        inorder(left[i])
    print(nodes[i], end="")
    if right[i]:
        inorder(right[i])


for tc in range(1,11):
    n = int(input())
    nodes = [0]*(n+1)
    left = [0]*(n+1)
    right = [0]*(n+1)

    for i in range(n):
        words = input().split()
        index = int(words[0])
        nodes[index] = words[1]
        if len(words) >= 3:
            left[index] = int(words[2])
            if len(words) == 4:
                right[index] = int(words[3])

    print(f"#{tc}", end=" ")
    inorder(1)
    print()

