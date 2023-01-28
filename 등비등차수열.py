a,b,c,n = input().split()
a = int(a)
b = int(b)
c = int(c)
n = int(n)




answer = a
for i in range(1, n):
    answer = answer * b + c
print(answer)