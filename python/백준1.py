#두 가지 방법 - 모두 str type을 반환
# 1. input()
# 개행 문자('\n') 전까지 입력 받음
# 2. sys.stdin.readline
# import sys 필요
# 개행 문자도 같이 입력 받음
# 반복문이 많을 경우 input() 함수가 오래 걸려서 시간초과 발생 가능

# a = input()
# print(a)

# import sys
# a = sys.stdin.readline()
# b = input()
# print(a, b, sep='')

#입력에 따라 다르게 받는 방법
# import sys
# result_int = sys.stdin.readline()
# print(type(result_int), result_int)
# print(type(int(result_int)), int(result_int))

# import sys
# a, b, c = map(int, sys.stdin.readline().split())
# print(a, b, c)

# import sys
#
# res_list = list(map(int, sys.stdin.readline().split()))
# print(res_list)

# import sys
#
# list_in_list = list()
# n = int(input())
# for i in range(n) :
#     list_in_list.append(list(map(int, sys.stdin.readline().split())))
# print(list_in_list)

# print("hi") # hi
# print() # \n
# print("hi", end="") # hello my name is
# print("hello", "my", "name", "is") # hi -> 설명 놓침 -> 개행 문자 없애주는 것?
# print("hello", "my", "name", "is", sep="") # hellomynameis
# print("hello", "my", "name", "is", sep="\n")
# #hello
# #my
# #name
# #is

# A = int(input())
# B = int(input())
# print(A+B)

# a = 5
# if a + 10 < 15:
#     print("참")
# else:
#     print("거짓")

# a = 3
# if (5 <= a) and (a < 10):
#     print("참")
# else:
#     print("거짓")

# N = input()
# N = int(N)
# print(type(N), N)
#
#
# N = int(input())
# if N % 2 == 0:
#     print("짝수")
# else:
#     print("홀수")

# N = int(input())
# if 90<=N<=100:
#     print('A')
# elif 80<=N:
#     print('B')
# elif 70<=N:
#     print('C')
# elif 60<=N:
#     print('D')
# else:
#     print('F')


# A, B = map(int, input().split())
# print(A + B)
# print(A - B)
# print(A * B)
# print(A // B)
# print(A % B)

# A = int(input())
# B = int(input())
# print(A+B)
# print(A-B)
# print(A*B)
# print(A/B)
# print(A%B)

# a = int(input())
#
# for i in range(9):
#     print(a, "*", i, "n", a * (i+1))

# arr = ['a', 'b', 'c', 'd']
#
# for idx, val in enumerate(arr):
#     print(idx, val)

# N=5
# for y in range(0, 5):
#     for x in range(0, y + 1):
#         print("(", y , x, ")", end='')
#     print(end='\n')

# N=int(input())
# for y in range(0, N):
#     for x in range(0, y + 1):
#         print('*', end='')
#     print()


# a = int(input())
# for i in range(9):
#     print(a, '*', i+1, '=', a*(i+1))

# a=1
# b=0
# n=int(input())
# for i in range(n+1):
#     b=a+i
#     print(a+b)
#     a=(a+b)

# n = int(input())
# a = 1
# for i in range(n+1):
#     a = a+i
# print(a-1)

# n = int(input())
# a = 0
# for i in range(1, n+1):
#     a = a+i
# print(a)

# cnt = int(input())
# numbers = list(map(int, input().split()))
# print(min(numbers),max(numbers))

# A, B = map(int, input().split())
# if A > B :
#     print('>')
# elif A < B :
#     print('<')
# else :
#     print('==')

# year=int(input())
# if((year%4==0 and year % 100!=0) or year % 400 == 0):
#     print('1')
# else:
#     print('0')

# x= int(input())
# y= int(input())
# if x > 0 and y > 0 :
#     print('1')
# elif x < 0 and y > 0 :
#     print('2')
# elif x < 0 and y < 0 :
#     print('3')
# else:
#     print('4')

# H, M = map(int, input().split())
# if M < 45 :
#     if H == 0 :
#         H = 23
#         M += 60
#     else :
#         H -= 1
#         M += 60
# print(H, M-45)

# hour, min = map(int, input().split())
# c = int(input())
#
# hour += c // 60
# min += c % 60
#
# if(min >= 60):
#     min -= 60
#     hour += 1
#
# if(hour >= 24):
#     hour -= 24
#
# print(hour, min)

# for _ in range(int(input())//4):
#     print("long", end=" ")
# print("int")

# a=int(input())
# for i in range(1,a+1):
#     print(" "*(a-i) + "*"*i)

# n=int(input())
# for i in range(n,0,-1):
#     print("*"*i)

# a=int(input())
# for i in range(a,0,-1):
#     print(" "*(a-i) + "*"*i)

# a=int(input())
# for i in range(1,a+1):
#     print(" "*(a-i)+"*"*((2*i)-1))

# a=int(input())
# for i in range(a,0,-1):
#     print(" "*(a-i)+"*"*((2*i)-1))

# a=int(input())
# for i in range(1,a):
#     print(" "*(a-i)+"*"*(2*i-1))
# for i in range(a,0,-1):
#     print(" "*(a-i)+"*"*(2*i-1))

# a=int(input())
# for i in range(1,a):
#     print("*"*i+" "*2*(a-i)+"*"*i)
# for i in range(a,0,-1):
#     print("*"*i+" "*2*(a-i)+"*"*i)

# x = int(input())
# for i in range(1, x + 1):
# 	print((" " * (i - 1)) + "*" * (2 * (x - i) + 1))
# for i in range(2, x + 1):
# 	print(" " * (x - i) + "*" * (2 * i - 1))

# x=int(input())
# for i in range(1,x+1):
#     print((" "*(x-i))+"*"*i)
# for i in range(1,x):
#     print((" "*i)+"*"*(x-i))