T= int(input())
for tc in range(1, T+1):
    n, q = map(int, input().split())
    box = [0]*(n+1)

    for i in range(1, q+1):
        l, r = map(int, input().split())
        for j in range(l, r+1):
            box[j] = i

    print(f"#{tc}", end=" ")
    for k in range(1, n+1):
        print(box[k], end=" ")
    print()