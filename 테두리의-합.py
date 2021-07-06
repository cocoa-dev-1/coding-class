n = int(input())
a = 0
main_list = []
sub_list = []
for i in range(1, n*n+1):
    sub_list.append(i)
    if len(sub_list) == n:
        main_list.append(sub_list)
        sub_list = []

print(main_list)

for i in range(len(main_list)):
    if i == 0 or i == len(main_list)-1:
        a += sum(main_list[i])
    else:
        for j in range(len(main_list[i])):
            if j == 0 or j == len(main_list[i])-1:
                a += main_list[i][j]

print(a)