row, col, query = map(int, input().split())
main_dic = {}
change_dic = {}
change_list = []
sub_dic = {1: (0,1), 2: (1,0), 3: (0,-1), 4: (-1,0)}
count = 0
go_to = 0

def direction():
    global go_to
    go_to += 1
    if go_to > 4:
        go_to = 1
    return sub_dic[go_to]

for i in range(row):
    for j in range(col):
        count += 1
        if (i+1,j+1) in main_dic:
            continue
        main_dic[(i+1,j+1)] = count

print(main_dic)

for _ in range(query):
    go_to = 0
    change_dic = {}
    x1, y1, x2, y2 = map(int, input().split())
    coords_list = [(x1, y1), (x2, y2), (x2, y1), (x1, y2)]
    dir = direction()
    sub_x1 = x1
    sub_y1 = y1
    while True:
        main_x1 = sub_x1
        main_y1 = sub_y1
        sub_x1 = main_x1 + dir[0]
        sub_y1 = main_y1 + dir[1]
        if (sub_x1, sub_y1) in change_dic:
            print(change_dic, sub_x1, sub_y1)
            break
        else:
            change_dic[(sub_x1,sub_y1)] = main_dic[(main_x1,main_y1)]
        if (sub_x1, sub_y1) in coords_list:
            dir = direction()

    result = list(change_dic.values())
    change_list.append(min(result))

    for k, v in change_dic.items():
        main_dic[k] = v

print(change_list)
            
        
            
    
    