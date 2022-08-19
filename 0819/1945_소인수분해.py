# 소인수분해
# n이 1이 될때까지 진행한다.

T = int(input())

for tc in range(1, T+1):
    a,b,c,d,e = 0,0,0,0,0

    n = int(input())
    while n != 1:
        if n%2 == 0:
            a += 1
            n = n//2

        if n%3 == 0:
            b += 1
            n = n//3

        if n%5 == 0:
            c += 1
            n = n//5

        if n%7 == 0:
            d += 1
            n = n//7

        if n%11 == 0:
            e += 1
            n = n//11
    print(f"#{tc}", end=" ")
    print(a, end=" ")
    print(b, end=" ")
    print(c, end=" ")
    print(d, end=" ")
    print(e)
