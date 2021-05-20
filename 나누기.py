mainInt = int(input())
sumInt = int(input())

result1 = mainInt // 100 * 100
result2 = result1 + (sumInt-(result1 % sumInt))
finalResult = result2 % 100
if finalResult < 10:
    finalResult = '0{0}'.format(finalResult)
print(finalResult)