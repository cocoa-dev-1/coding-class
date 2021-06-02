n = int(input())

def funcOne(a):
    a = int(a/2)
    if a != 1:
        print(a)
        if a % 2 ==0:
            funcOne(a)
        else:
            funcTwo(a)

def funcTwo(a):
    a = int(a*3 + 1)
    if a != 1:
        print(a)
        if a % 2 ==0:
            funcOne(a)
        else:
            funcTwo(a)

print(n)
if n % 2 == 0:
    funcOne(n)
else:
    funcTwo(n)