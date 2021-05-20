resultList = [0]

for i in range(4):
    first1, first2 = map(int, input().split())
    resultList.append(resultList[i]+(first2-first1))

print(max(resultList))