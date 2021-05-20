inConst = int(input())
inLet = int(input())
inNum = int(input())

inCount = 0

getAmount = inNum - inLet

if getAmount <= 0:
    print('-1')
else:
    total = inConst//getAmount
    print(total+1)