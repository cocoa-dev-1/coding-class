n = int(input())
x, y = map(int, input().split())
main_list = []

def get_num(a):
    return a if a > 0 else -a

def draw_list(x, y):
    for i in range(n):
        for j in range(n):
            try:
                print(get_num(j-(y-1))+get_num(i-(x-1))+1, end=' ')
            except:
                print('error')
                pass
        print('')

for i in range(n):
    main_list.append([0 for _ in range(n)])

for i in main_list:
    print(i)

draw_list(x, y)
