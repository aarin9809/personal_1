a, b = input().split()
a = int(a)
b = int(b)

small = min(a, b)
big = max(a, b)

for i in range(small, big + 1):
    print(i, end=" ")

if a < b:
    print("a<b")
    for i in range(a, b+1):
        print(i, end=" ")
else:
    print("a>=b")
    for i in range(b , a+1):
        print(i, end=" ")