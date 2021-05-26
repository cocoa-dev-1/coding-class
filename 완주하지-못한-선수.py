a = input().split()
b = input().split()
a_dic = {}
for i in a:
    if i in b:
        continue
    if i in a_dic:
        continue
    a_dic[i] = i

print(a_dic.values())
