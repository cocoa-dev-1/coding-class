
n1, n2 = map(int, input().split())
x, y, d = map(int, input().split())

main_list = [list(map(int, input().split())) for _ in range(n1)]
main_dict = {}
sub_list = []
x_list = [-1,0,1,0]
y_list = [0,-1,0,1]

for i in range(n1):
    for j in range(n2):
        main_dict[(i,j)] = 0
print(main_dict)

def turn_left():
    global d
    #d = (d+3)%4
    d += 1
    if d == 4:
        d = 0
turn_left()
count = 1
count_four = 0
main_dict[(x,y)] = 1
while True:
    turn_left()
    if count_four > 4:
        nx = x + (-x_list[d])
        ny = y + (-y_list[d])
        res = main_list[nx][ny]
        if res == 1:
            break
        else:
            x = nx
            y = ny
            count_four = 0

    count_four += 1
    nx = x + x_list[d]
    ny = y + y_list[d]
    if nx >= 0 and ny >= 0 and nx < n1 and ny < n2:
        land_or_sea = main_list[nx][ny]
        if land_or_sea == 0 and main_dict[(nx,ny)] == 0:
            x = nx
            y = ny
            main_dict[(nx,ny)] = 1
            count += 1
            count_four = 0
            print(x,y)
    
print(count)
    
        


