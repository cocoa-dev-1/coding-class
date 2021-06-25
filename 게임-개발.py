
n1, n2 = map(int, input().split())
x, y, looking = map(int, input().split())

looking_ditc = {0:1}

main_list = [list(map(int, input().split())) for _ in range(n1)]

for i in main_list:
    print(i)