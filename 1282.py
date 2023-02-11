#n이 입력이되고
#
import math


n = int(input())
k = 1
t = 1

for i in range(1, n):
    if i * i > n:
        i - 1
        target = i -1
        k = n - target * target
        t = target
        break
print(k ,t)