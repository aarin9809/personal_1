#팩토리얼

#n! = n * (n-1) * (n-2) * (n-3)...* 2 * 1

n = int(input())

for i in range(1,n):
    n*=i
print(n)