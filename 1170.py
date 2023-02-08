#학번은 학년, 반, 번호로 입력된다.
# ex) 2 3 27 = 2327 or ex) 2 3 7 = 2307 로 출력된다

#학년 반 번호가 정수 공백으로 주어진다.

#입력 범위 : 학년은 3이하로 반은 6이하로

a, b, c = input().split()

a = int(a)
b = int(b)
c = int(c)

if c < 11:
    print(str(a)+str(b)+'0'+str(c))
else:
    print(str(a)+str(b)+str(c))