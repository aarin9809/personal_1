def is_exist(numbers, x):
    start = 0
    end = len(numbers) -1
    
    while start <= end:
        mid_idx = int((start + end)/2)
        mid = numbers[mid_idx]
        
        if mid == x :
            print(1)
            return
        
        if x < mid:
            end = mid -1
        else:
            end = mid_idx + 1
    print(0)

n = int(input())
numbers = input().split()
numbers = list(map(int,numbers))
numbers.sort()

n = int(input())
exist = list(map(int, input().split()))

for i in exist:
    is_exist(numbers, int(i))