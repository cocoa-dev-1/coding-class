s = input()

dic = {}

for i in 'abcdefghijklmnopqrstuvwsyxz':
    dic[i] = 0

for i in s:
    if i in dic:
        dic[i] += 1

for i in 'abcdefghijklmnopqrstuvwsyxz':
    print(dic[i], end=' ')
