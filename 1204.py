# n = input()
#print(n, end="")  #개행 없음을 이용해서 프린트문을 따로 사용하여 출력을 붙이는 방법도 있음
#
#if len(n) == 1:
#    if int(n) == 1:
#        print("st")
#    elif int(n) == 2:
#        print("nd")
#    elif int(n) == 3:
#        print("rd")
#    else:
#        print("th")
#elif len(n) == 2:
#    if int(n) == 11 or int(n) == 12 or int(n) == 13:
#        print("th")
#    elif n[1] == "1":
#        print("st")
#    elif n[1] == "2":
#        print("nd")
#    elif n[1] == "3":
#        print("rd")
#    else:
#        print("th")
#
#else:
#    print("잘못된 입력")
#################################정수형으로 풀어보기#############################
n = int(input())

print(n, end="")

if n == 11 or n ==12 or n == 13:
    print("th")

elif n % 10 == 1:
    print("st")
elif n % 10 == 2:
    print("nd")
elif n % 10 == 3:
    print("rd")
else:
    print("th")