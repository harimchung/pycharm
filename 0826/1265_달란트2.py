T = int(input())
for tc in range(1, T+1):
    n, p = map(int, input().split())

    # p개의 방만큼 방을 만든다.
    rooms = [0 for _ in range(p)]

    # n개 만큼 분배한다.
    for i in range(n):
        a = rooms.pop(0)
        a += 1
        rooms.append(a)
    ans = 1
    for i in rooms:
        ans *= i
    print(f"#{tc} {ans}")