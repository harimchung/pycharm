T = int(input())
for tc in range(1,T+1):
    # 정수 n이 주어진다.
    n = int(input())
    station = [0]*5001

    # n 줄만큼 ai, bi가 공백으로 구분되어 주어진다.
    for _ in range(n):
        a, b = map(int, input().split())
        # a이상 b이하의 정류장에 +1씩 더해준다.
        for i in range(a, b+1):
            station[i] += 1


    print(f"#{tc}", end=" ")

    # P개의 버스 정류장 수가 주어진다.
    p = int(input())
    # 각 정류장에 몇 개의 버스노선이 다니는지 구하면 된다.
    for __ in range(p):
        c = int(input())
        print(station[c], end=" ")
    print()
