#정수를 매개변수로 받아서 각 자리 숫자의 합을 계산하는 함수를 작성하라.

#단, 나눗셈은 이용하지말것.
def sumOfDigit():
    a = input()

    list1 = list(a)

    list2 = list(map(int, list1))

    return sum(list2)

print(sumOfDigit())