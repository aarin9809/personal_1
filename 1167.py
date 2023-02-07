# 세개의 숫자가 공백으로 나뉘어 주어짐
# ex) 5 9 2 가 있다면, 두번째 숫자는 5

list1 = list(input().split())

list2 = list(map(int, list1))

list2.sort()

print(list2[1])