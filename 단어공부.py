Lang = input()
dic = {}

for i in Lang:
    if i.upper() in dic:
        dic[i.upper()] += 1
    else:
        dic[i.upper()] = 1

result_dic = {value:key for key, value in dic.items()}

result_count = list(dic.values()).count(max(list(dic.values())))
print(result_dic[max(list(dic.values()))]) if result_count == 1 else print('?')

