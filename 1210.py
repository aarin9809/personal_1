# 1. 치즈버거 : 400칼로리
# 2. 야채버거 : 340칼로리
# 3. 우유 : 170칼로리
# 4. 계란말이 : 100칼로리
# 5. 샐러드 : 70칼로리

#두가지 메뉴를 선택하고 칼로리의 합을 계산했을때, 합이 500보다 크면 angry를
#500이하면 no angry를 출력하라

# 숫자 두개를 골랐을때 -> 공백을 기준으로 입력된다.
# 그 두개에 해당되는 값을 연산해서 출력한다.
# 딕셔너리를 사용해야하는건지?
# sum 값을 0으로 초기화 시켜놓고, 번호를 고를때마다 sum값에다 해당 칼로리를 추가 시키는?
# 그렇게 해서 최종적으로 print(sum)이 되게끔?

#a, b = input().split()

#sum = 0
#a = int(a)
#b = int(b)

#if a == 1:
#    sum += 400
#elif a == 2:
#    sum += 340
#elif a == 3:
#    sum += 170
#elif a == 4:
#    sum += 100
#elif a == 5:
#    sum += 70
#
#if b == 1:
#    sum += 400
#elif b == 2:
#    sum += 340
#elif b == 3:
#    sum += 170
#elif b == 4:
#    sum += 100
#elif b == 5:
#    sum += 70
#
#if sum > 500:
#    print("angry")
#else:
#    print('no angry')

a , b = input().split()

a = int(a)
b = int(b)

dict = {'cheeseburger': 400, 'vegeburger': 340, 'milk':170, 'eggroll':100, 'salad':70}

v = list(dict.values())

s = v[a-1] + v[b-1]


if s > 500:
    print('angry')
else:
    print('no angry')