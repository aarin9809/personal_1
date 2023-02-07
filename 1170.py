#학번은 학년, 반, 번호로 입력된다.
# ex) 2 3 27 = 2327 or ex) 2 3 7 = 2307 로 출력된다

#학년 반 번호가 정수 공백으로 주어진다.

#입력 범위 : 학년은 3이하로 반은 6이하로 번호는 30 이하로

a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

if a<=3 and b <= 6 and 10 <= c:
    print(a,b,c, end="")
elif a <=3 and b <= 6 and c<=10:
    print(a,b,c, end="")