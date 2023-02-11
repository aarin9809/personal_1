list1 = list(input().split())

list2 = list(map(int, list1))

list2.sort()

print(*list2)