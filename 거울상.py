main_list = []
result_list = []
canBePrint_list = ['b','d','q','p','i','o','v','w','x']
while True:
    i = input()
    if i == '#':
        break
    main_list.append(i[::-1])

for i in main_list:
    isVail = True
    main_str = ''
    for a in range(len(i)):
        if i[a] in canBePrint_list:
            if i[a] == 'b':
                main_str += 'd'
            elif i[a] == 'd':
                main_str += 'b'
            elif i[a] == 'q':
                main_str += 'p'
            elif i[a] == 'p':
                main_str += 'q'
            else:
                main_str += i[a]
        else:
            isVail = False
            result_list.append('INVALID')
            break
    if isVail:
        result_list.append(main_str)

for i in result_list:
    print(i)

    
        

