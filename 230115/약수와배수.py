#1부터 100까지 짝수면 '짝' 홀수면 '홀' 출력
#for n in range(1,101):
#    if n % 2 ==0:
#        print(n,'은 짝수입니다.')
#    else:
#        print(n,'은 홀수입니다.')
#
#n=1
#while n<101:
#    if n % 2 ==0:
#        print(n,'은 짝수입니다.')
#    else:
#        print(n,'은 홀수입니다.')
#    n=n+1

#1부터 100까지 2의 배수 and 7의 배수 출력

#n=1
#while n <=100:
#    if n % 2 ==0 and n % 7 == 0:
#        print(n)
#    n+=1

#10의 약수 출력(1,2,5,10)
#for i in range(1,101):
#    if 100 % i == 0:
#        print(i, '= 약수입니다')

i = int(input())
for n in range(1,i+1):
    if i % n == 0:
        print(n, '= 약수입니다')