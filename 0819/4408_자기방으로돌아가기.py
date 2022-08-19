T = int(input())
for tc in range(1, T+1):

    n = int(input())
    corridor = [0] * 401
    for _ in range(n):
        start, end = map(int, input().split())
        if end < start:
            start, end = end, start

        if start%2 == 0:
            start = start-1
        if end%2 == 1 :
            end = end+1

        for i in range(start, end+1):
            corridor[i] += 1
    cnt = max(corridor)

    print(f"#{tc} {cnt}")