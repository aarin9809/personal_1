list1 = list(input().split())

list2 = list(map(int, list1))
if list2.count(1) == 0:
    print("모")
elif list2.count(1) == 1:
    print("도")
elif list2.count(1) == 2:
    print("개")
elif list2.count(1) == 3:
    print("걸")
elif list2.count(1) == 4:
    print("윷")