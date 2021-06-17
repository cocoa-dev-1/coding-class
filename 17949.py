from abc import abstractproperty


main_str = input()
n = int(input())
result_types = list(input().split())
type_list = []
last_type = 0

for i in result_types:
    if i == 'char':
        type_list.append(2)
    elif i == 'int':
        type_list.append(8)
    elif i == 'long_long':
        type_list.append(16)

for i in type_list:
    print(int(main_str[last_type:last_type+i], 16), end=' ')
    last_type += i