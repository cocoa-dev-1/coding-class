import random

main_list = []

for i in range(9):
    a = [random.randint(0,1) for _ in range(9)]
    main_list.append(a)

for i in main_list:
    print(i)

i, j = map(int, input().split())

if main_list[i-1][j-1] == 1:
    print(-1)
else:
    count = 0
    k, l = i-1, j-1
    if k == 0 and l == 0:
        sub_list = [main_list[k][l+1], main_list[k+1][l], main_list[k+1][l+1]]
        for i in sub_list:
            count += 1 if i == 1 else 0
    elif k == 8 and l == 8:
        sub_list = [main_list[k][l-1], main_list[k-1][l], main_list[k-1][l-1]]
        for i in sub_list:
            count += 1 if i == 1 else 0
    elif k == 8 and l == 0:
        sub_list = [main_list[k-1][l], main_list[k-1][l+1], main_list[k][l+1]]
        for i in sub_list:
            count += 1 if i == 1 else 0
    elif k == 0 and l == 8:
        sub_list = [main_list[k][l-1], main_list[k+1][l-1], main_list[k+1][l]]
        for i in sub_list:
            count += 1 if i == 1 else 0
    elif k == 8:
        sub_list = [main_list[k][l-1], main_list[k-1][l-1], main_list[k-1][l], main_list[k-1][l+1], main_list[k][l+1]]
        for i in sub_list:
            count += 1 if i == 1 else 0
    elif l == 8:
        sub_list = [main_list[k+1][l], main_list[k+1][l-1], main_list[k][l-1], main_list[k-1][l-1], main_list[k-1][l]]
        for i in sub_list:
            count += 1 if i == 1 else 0
    elif k == 0:
        sub_list = [main_list[k][l-1], main_list[k+1][l-1], main_list[k+1][l], main_list[k+1][l+1], main_list[k][l+1]]  
        for i in sub_list:
            count += 1 if i == 1 else 0
    elif l == 0:
        sub_list = [main_list[k-1][l], main_list[k-1][l+1], main_list[k][l+1], main_list[k+1][l+1], main_list[k+1][l]]
        for i in sub_list:
            count += 1 if i == 1 else 0
    else:
        sub_list = [main_list[k][l-1], main_list[k-1][l-1], main_list[k-1][l], main_list[k-1][l+1], main_list[k][l+1], main_list[k+1][l+1], main_list[k+1][l], main_list[k+1][l-1]]
        for i in sub_list:
            count += 1 if i == 1 else 0
    print(count)