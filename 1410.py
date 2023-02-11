# 1차원배열문제

# 괄호로 이루어진 문자열이 입력된다
# 여는 괄호의 갯수와 닫힌 괄호의 갯수를 출력한다.

# 열기 괄호 갯수 == 닫긴 괄호 갯수

list1 = list(input())

a = list1.count('(')

b = list1.count(')')

print(a, b)