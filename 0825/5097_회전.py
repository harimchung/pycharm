T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    num = list(map(int, input().split()))

    for _ in range(m):
        a = num.pop(0)
        num.append(a)

    b = num.pop(0)
    print(f"#{tc} {b}")