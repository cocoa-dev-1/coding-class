a = 3
b = 5

for i in range(a*b, 101, a*b) :
    print(i)


c = int(input())
d = int(input())
if c < d :
    for i in range(c*d,101,c*d):
        print(i)

st = 'This is python'.lower()
e = 0
for i in st:
    if i == 't' :
        e = e + 1

if e == 0 : 
    print(e - 1)
else:
    print(e)




f = input()
g = input()
h = 0

for i in f :
    if i == g:
        h += 1

print(-1) if h == 0 else print(h) 

