mainLoop = int(input())

mainList = []

for _ in range(mainLoop):
    a, b = map(int, input().split())
    sumResult = (a**b)%10
    if sumResult == 0:
        sumResult = 10
    mainList.append(sumResult)

for i in mainList:
    print(i)