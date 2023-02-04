# 1, 10, 2, 20, 3, 30, 4, 40 ...
# 존의 번호 k 밥의 번호 h 공백으로 분리되어 입력받는다.
# 예를들어 존이 1번 밥이 2번을 뽑았다면, 금액의 합은 11이 된다.
# 각각 받은 돈을 받고 k + h를 프린트하면 된다.


# 규칙을 변수로 바꾸어 보자면
# n, n*10, n+1, (n+1)*10, ... 이 된다.
# n을 하나씩 늘리는 식으로 반복문을 작성해보자.
# 홀수번호를 뽑으면 작은돈
# 짝수돈을 뽑으면 큰돈
a, b = input().split()
a = int(a)
b = int(b)


#i = 1
#multiple = 1
#end = max(a,b)
#flag = True
#sum = 0
#
#
#while True:
#    print(i,"번째")
#    if flag == True:
#        if i == a:
#            sum += multiple
#        if i == b:
#            sum += multiple
#
#        multiple *= 10
#        flag = False
#
#    else:
#        if i == a:
#            sum += multiple
#        if i == b:
#            sum += multiple
#
#        multiple = multiple // 10
#
#
#
#        multiple+=1
#        flag = True
#
#
#    if i == end:
#        break
#
#    i += 1






end = max(a,b)
donation = 1
sum = 0
i = 1
flag = True
while True:
    if flag:
        if i == a or i == b:
            sum += donation
        donation *= 10
        flag = False



    else:
        if i == a or i == b:
            sum += donation
        donation = donation // 10

        donation += 1
        flag = True



    if i == end:
        break

    i += 1

print(sum)

































