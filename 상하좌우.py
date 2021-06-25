from os import cpu_count


n = int(input())
n_list = list(input().split())

main_list = [[0]*n for _ in range(n)]
main_dict = {'R':[0,1],'L':[0,-1],'U':[-1,0],'D':[1,0]}

def get_coords(coord_list):
    x, y = 0, 0
    for i in coord_list:
        if x + main_dict[i][0] < 0 or y + main_dict[i][1] < 0:
            continue
        try:
            k = main_list[x + main_dict[i][0]][y + main_dict[i][1]]
            x += main_dict[i][0]
            y += main_dict[i][1]
            print(x, y)
        except:
            pass
    return x+1, y+1

def get_coords_2(coord_list):
    global n
    x, y = 1, 1
    count = 0
    for i in coord_list:
        nx = x + main_dict[i][0]
        ny = y + main_dict[i][1]
        if nx > 0 and ny > 0 and nx <= n and ny <= n:
            x = nx
            y = ny
    return x, y


a, b = get_coords_2(n_list)
print(a, b)
        