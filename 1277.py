n = int(input())

a = list(input().split())

b = list(map(int,a))

mid = int(n / 2 + 1)
print(b[0],b[mid-1],b[n-1])