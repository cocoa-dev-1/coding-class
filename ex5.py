inputInt = int(input())
b = 0

def getIntLen(n):
    n = str(n)
    return len(n)

while True:
    a = getIntLen(inputInt)
    if a == 1:
        break

    for i in range(1,a+1):
        if i == 1:
            b += inputInt % 10
            inputInt = inputInt // 10


print(inputInt)