# class stack:
#     def __init__(self):
#         self.items = []
#
#     def push(self, item):
#         self.items.append(item)
#         print(f"push {item}")
#
#     def pop(self, item):
#         item = self.items.pop(-1)
#         print(f"pop {item}")
#         return item
#
#     # 3. peep top에 있는 원소 반환하기
#     def peek(self):
#         print(f"peek {self.items[-1]}")
#         return self.items[-1]
#
#     # 4. stack 이 비어있는지 확인하는 연산
#     # 비어있으면, True를 반환한다.
#     def isEmpty(self):
#         return not self.items
#
# # 스택 생성하기
# my_stack = stack()
#
# # 원소 삽입
# for i in range(5):
#     my_stack.push(i)
#
# # 스택의 꼭대기에 있는 원소 반환
# print(my_stack.peek())
#
# # 스택에서 원소 제거
# for i in range(5):
#     my_stack.pop(i)

# def f(n):
#     if n > 5:
#         return
#     else:
#         print(f"{n} in")
#         f(n+1)
#         print(f"{n} out")
# f(1)

def fibo(n):
    if n < 2 :
        return n
    else :
        return fibo(n-1) + fibo(n-2)

# print(fibo(100))

def fibo1(n):
    global memo
    if n >=2 and len(memo) <= n:
         memo.append(fibo1(n-1) + fibo1(n-2))
    return memo[n]

memo = [0,1]

# print(fibo1(100))

def fibo2(n):
    f = [0, 1]

    for i in range (2, n+1):
        f.append(f[i-1] + f[i-2])

    return f[n]

print(fibo2(100))