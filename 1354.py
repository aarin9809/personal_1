#중첩 반복문
#역삼각형 별찍기

#n의 값이 주어지면
#길이 n의 역삼각형을 출력한다
#ex) n = 3 이면  3 2 1 갯수 순으로 각기 다른 문장에 별을 찍는다.
# n에 따라 찍히는 문장수와 별의 갯수가 정해진다.
n = int(input())
#print('*'*5)
#print('*'*4)
#print('*'*3)
#print('*'*2)
#print('*'*1)
# 변하는 숫자는 곱해지는 수가 하나씩 줄어들고,
# 프린트문은 총 n번 반복된다.

for i in range(n): #프린트문 n번 반복하는 역할
    for j in range(n-i): #곱해지는 수를 반복해서 1씩 줄이는 역할
        print('*', end="")
    print("")
#풀이
# 17line 0부터 카운트해서 i에 들어감
# 18line 5-0해서 j에 5가 들어가서 별이 빈칸없이 5번찍히고
# 20번 라인에서 한줄 건너뜀
# 다시 17line에서 1이 들어감
# 5-1=4 해서 j에 4가 들어감
# 별이 빈칸없이 4번찍히고 한줄 건너뜀
# range(n)이므로 0~4까지 5번 반복함
# n-i 과정에서 5-0 부터 5-4까지 결과값대로 별을 찍어냄
