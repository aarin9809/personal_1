psd = list(input())

#print(psd)  #['T', 'E', 'S', 'T']

a = int(ord(psd[0]) + 2)
b = int(ord(psd[1]) + 2)
c = int(ord(psd[2]) + 2)
d = int(ord(psd[3]) + 2)

print(chr(a)+chr(b)+chr(c)+chr(d))

e = int(ord(psd[0]) * 7 % 80 + 48)
f = int(ord(psd[1]) * 7 % 80 + 48)
g = int(ord(psd[2]) * 7 % 80 + 48)
h = int(ord(psd[3]) * 7 % 80 + 48)

print(chr(e) + chr(f) + chr(g) + chr(h))