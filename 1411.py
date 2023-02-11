# 빠진 카드 찾기

#첫번째 입력에는 카드가 숫자 몇까지 인지를 정하는 숫자를 입력한다
#두번째 입력부터는 숫자를 입력하면서 반복하여 빼낸다.
# 남은 숫자를 출력한다.

n = int(input())
b = 0

list1 = []

for i in range(1, n+1):
    list1.append(i)

while n-1>b:
    a = int(input())
    list1.remove(a)
    if len(list1) == 1:
        break
print(*list1)