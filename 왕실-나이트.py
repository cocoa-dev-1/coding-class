
n = input()

main_list = [[0]*8 for _ in range(8)]
a_to_z = [chr(i) for i in range(97, 123)]

def get_count(x,  y):
    x = a_to_z.index(x)
    count = 0
    for i in range(y-2, y+3):
        for j in range(x-2, x+3):
            if (j == x and i == y) or (j < 0 or i < 0):
                continue
            if j == x and abs(y-i) == 2:
                print('a',j,i)
                if j-1 >= 0:
                    try:
                        k = main_list[i][j-1]
                        count +=1
                    except:
                        print('2')
                        pass
                if j+1 >= 0:
                    try:
                        k = main_list[i][j+1]
                        count += 1
                    except:
                        print('22')
                        pass
            elif y == i and abs(x-j) == 2:
                print('b',j,i)
                if i-1 >= 0:
                    try:
                        k = main_list[i-1][j]
                        count +=1
                    except:
                        print('1')
                        pass
                if i+1 >= 0:
                    try:
                        k = main_list[i+1][j]
                        count += 1
                    except:
                        print('11')
                        pass
    return count
    

print(get_count(n[0], int(n[1])-1))