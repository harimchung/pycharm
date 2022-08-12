# def strlen(a):
#     cnt = 0
#     i = 0
#     while a[i] != '\0':
#         cnt += 1
#         i += 1
#     return cnt
#
# a = [ 'a', 'b', 'c', '\0']
# print(strlen(a))
#
# # s1 = list(input())
# # print(s1) # h, e, l, l ,o 이렇게 하나씩 따로 들어가게 된다.
#
# def my_reverse(s):
#     empty_string = ""
#     for i in range(-1, -len(s)-1, -1):
#         empty_string += s[i]
#     return empty_string
#
# s = "Reverse this strings"
# print(my_reverse(s))
#
# def my_reverse_2(s):
#     list_s = list(s)
#     n = len(list_s)
#     for i in range(n//2):
#         list_s[i], list_s[n-i-1] = list_s[n-i-1], list_s[i]
#     return "".join(list_s)
#
# print(my_reverse_2(s))
#
# s1 = 'abc'
# s2 = 'abc'
# s3 = 'def'
# s4 = s1
# s5 = s1[:2] + 'c'
#
# # print(s1==s2) # 이것은 맞다. 값은 같다.
# # print(s1 is s2) # 문자열을 사용하면 list와 다르게, 같은 문자열을 써버리면 동등한 주소에서 데리고 온다.
# # print(s1 is s4) # 이것은 얕은 복사이기 때문에 복사해온 것이라 주소까지 같다.
# # print(s5) # 이거은 abc가 될 것 같다.
# # print(s1 == s5)
# # print(s2 == s5)
# # print(s1 == s5)
# # print(s2 is s5) # 주소도 다르다.
#
#
# def my_strcmp (str1, str2):
#     i = 0
#     n = len(str1)
#     m = len(str2)
#     if n <= m:
#         short = n
#     elif m < n:
#         short = m
#     if str1 == str2:
#         return 0
#     while i < short-1:
#         if ord(str1[i]) < ord(str2[i]) :
#             return -1
#             break
#         elif ord(str1[i]) > ord(str2[i]) :
#             return 1
#             break
#         elif ord(str1[i]) == ord(str2[i]) :
#             i += 1
#
#
# # python 에서 문자 상에서 부등호 사용시 아스키코드 값으로 비교한다.
# def my_strcmp2 (s1, s2):
#     if s1 < s2:
#         return -1
#     elif s1 > s2:
#         return 1
#     else :
#         return 0
#
#
# def my_itoa(number):
#     i = 10
#     s = "" # 숫자를 문자로 바꾼 결과물
#     while number > 0:
#         mod = number % i
#         s += chr(ord('0') + mod)
#         number //= 10
#     return s[::-1]
#
# a = 1234
# print(my_itoa(a))
#
# p = "is"
# t = "This is a book~! "
# M = len(p) # 2
# N = len(t) # 16
#
# def BruteForce(p,t):
#     i = 0 # t의 인덱스
#     j = 0 # p의 인덱스
#     while j<M and i<N:
#         if t[i] != p[j] :
#             i = i -j
#             j = -1
#         i = i+1
#         j = j+1
#     if j == M :
#         return i - M
#     else :
#         return -1

def is_prime(n):
	for i in range(2,n):
		if n%i == 0:
			return False
	return True

print(is_prime(10))
print(is_prime(2))
print(is_prime(5))
print(is_prime(131))
print(is_prime(167))
print(is_prime(169))