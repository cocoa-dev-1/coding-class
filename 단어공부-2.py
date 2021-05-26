
dic = {}
result_list = []
for i in range(int(input())):
    name = input()
    if '{0},{1}'.format(name, ord(name[0])) in dic:
        dic['{0},{1}'.format(name, ord(name[0]))] += 1
    else:
        dic['{0},{1}'.format(name, ord(name[0]))] = 1

result_dic = {}
for key, value in dic.items():
    if value in result_dic:
        if int(result_dic[value].split(',')[1]) > int(key.split(',')[1]):
            result_dic[value] = key
    else:
        result_dic[value] = key

result_count = list(dic.values()).count(max(list(dic.values())))

print(result_dic[max(list(dic.values()))].split(',')[0])

    