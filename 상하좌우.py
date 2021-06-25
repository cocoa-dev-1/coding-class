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

a, b = get_coords(n_list)
print(a, b)
        