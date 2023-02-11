#학번은 학년, 반, 번호로 입력된다.
#각 숫자는 정수형으로 입력 된다.

#학년은 한자리 반은 두자리 번호는 세자리로 출력된다.

#경우의수
# 1. b가 한자리 c가 한자리 v
# 2. b가 한자리 c가 두자리 v
# 3. b가 두자리 c가 한자리 v
# 4. b가 두자리 c가 두자리 v
# 5. b가 한자리 c가 세자리
# 6. b가 두자리 c가 세자리


a, b, c = input().split()

a = int(a)
b = int(b)
c = int(c)

if b<10 and c<10:#b와 c가 한자리 숫자일때 경우
    print(str(a)+'0'+str(b)+'00'+str(c))
elif b<10 and 10<=c<100: #b가 한자리 c가 두자리
    print(str(a)+'0'+str(b)+'0'+str(c))
elif b<10 and 99<c<=999: #b가 한자리 c가 세자리
    print(str(a)+'0'+str(b)+str(c))
elif 10<=b<=20 and c<10:#b가 두자리 c가 한자리
    print(str(a)+str(b)+'00'+str(c))
elif 10<=b<=20 and 10<=c<100: #b와 c가 두자리일때
    print(str(a)+str(b)+'0'+str(c))
else:
    print(str(a)+str(b)+str(c))