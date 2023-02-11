# 어떤 한 숫자가 주어지면 소수인지 판별하는 프로그램
# 소수란 1과 자기자신만 약수를 가지는 수
# 소수를 판별하려면?
# -> 약수가 나오는 경우의 반대 경우를 생각하면 된다.


n = int(input())

a = True            #소수 판별 변수를 True로 초기화

for i in range(2,n): #2부터 n전까지
    if n % i == 0:   # 소수가 아니란 판별
        a = False    # 소수가 아닐땐 False 값을 리턴한다.
                     # 이 식이 곧 소수 판단기준이 된다.

if a == True:
    print('prime')
else:
    print('not prime')