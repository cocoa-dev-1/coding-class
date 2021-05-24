#List = list(input().split('[')[1].split(']')[0].split(','))
List = eval(input())
dic = {}

for i in List:
    if i in dic:
        del dic[i]
    else:
        dic[i] = int(i)

print(sum(dic.values()))

