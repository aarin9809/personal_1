# n명의 학생과 점수를 입력받는다
# a에는 이름이 b에는 점수를 입력받는다.
# 딕셔너리를 써야하나...
#

n = int(input())

d = {}

for i in range(n):
    name, grade = input().split()
    d[int(grade)] = name

s = sorted(d)

print(d[s[-3]])