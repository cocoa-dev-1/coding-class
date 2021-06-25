main_list = []
inp = int(input())
map1_list = list(map(int, input().split()))
map2_list = list(map(int, input().split()))

for i in range(len(map1_list)):
    main_list.append(map1_list[i] | map2_list[i])

for i in main_list:
    a = bin(i)[2:]
    print(a.zfill(inp-len(a)).replace('1', "#").replace('0', ' '))
    