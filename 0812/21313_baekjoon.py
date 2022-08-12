n = int(input())
if n % 2 : # 2로 나눈 나머지가 1인경우, 즉 True인 경우, 즉 홀수 인 경우에 실행한다.
    print("1 2 "*(n//2)+"3")
else:
    print("1 2 "*(n//2))