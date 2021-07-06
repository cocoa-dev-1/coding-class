n, m = map(int, input().split())
main_list = [[0]*m for _ in range(n)]
dir_dic = {1: (0,1), 2: (1,0), 3: (0,-1), 4: (-1,0)}
dir_count = 0
turn_count = 0
count = 0
x, y = 0, 0
dir = [0, 0]

def direction():
    global dir_count
    dir_count += 1
    if dir_count > 4:
        dir_count = 1
    return dir_dic[dir_count]


while True:
    if turn_count > 4:
        break
    nx = x + dir[0]
    ny = y + dir[1]
    if nx == n or ny == m:
        dir = direction()
        turn_count += 1
        continue
    a = main_list[nx][ny]
    if a != 0:
        dir = direction()
        turn_count += 1
        continue
    x = nx
    y = ny
    count += 1
    main_list[x][y] = count
    turn_count = 0

for i in main_list:
    print(i)
    

