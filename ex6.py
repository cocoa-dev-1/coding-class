inConst = int(input())
inLet = int(input())
inNum = int(input())

inCount = 0

while True:
    if inLet >= inNum:
        print('손익분기점이 없습니다.')
        break
    inCount += 1
    PayAmount = inConst + inLet*inCount
    SellAmount = inCount*inNum
    if (SellAmount - PayAmount) > 0:
        print('손익분기점')
        print('판매량: ', inCount)
        break