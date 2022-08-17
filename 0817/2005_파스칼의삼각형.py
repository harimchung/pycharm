# def f(n):
#     if n == 1:
#         return [1]
#     if n == 2:
#         return [1,1]
#     else :
#         empty_list = [1] * n
#         for i in range (1, n-1):
#             empty_list[i] = f(n-1)[i-1] + f(n-1)[i]
#     return empty_list
#
#
# T = int(input())
# for tc in range(1,T+1):
#     n = int(input())
#     print(f"#{tc}")
#     for i in range(1,n+1):
#         print(" ".join(map(str, f(i))))

# 파스칼 삼각형의 첫 요소와 끝 요소는 모두 1이다.
# 총 입력의 길이가 10이 최대이다.

# 우선 [1]이 n개 만큼 있는 10줄짜리 리스트를 만든다.
pascal = [ [1]*n for n in range (1,11) ]

# 2번째 인덱스, 즉 [1,2,1] 부터 윗줄의 요소와의 합을 구하는
# 반복문을 짰다.
for i in range(2,10):
    for j in range (1,i):
        pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    print(f"#{tc}")
    for i in range(0,n):
        # join은 str에서밖에 작동하지 않기 때문에 숫자를 전부 str으로 바꿔주는 작업이 필요하다.
        print(" ".join(map(str, pascal[i])))