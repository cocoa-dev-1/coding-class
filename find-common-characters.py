List = eval(input())

dic = {}
final_list = []

for i in range(len(List)):
    print(list(set(List[i])))
    b = list(set(List[i]))
    for a in b:
        if a in dic:
            dic[a].append(List[i].count(a))
        else:
            dic[a] = [List[i].count(a)]
print(dic)

for i in dic:
    if len(dic[i]) == len(List):
        for _ in range(min(dic[i])):
            final_list.append(i)
print(final_list)
        
    