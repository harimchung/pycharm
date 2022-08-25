for _ in range(10):
    tc = int(input())

    q = list(map(int, input().split()))

    number = 1

    while True:
        item = q.pop(0)
        item -= number
        if item <= 0:
            item = 0
            q.append(item)
            break
        q.append(item)
        number += 1
        if number > 5:
            number = 1

    print(f"#{tc}", end=" ")
    while q:
        print(q.pop(0), end=" ")
    print()
