import random

main_list = []

def get_count_of_boom(a, b):
    count = 0
    try:
        k = main_list[a][b]
    except:
        pass
    if k == 1:
        return -1
    for c in range(a-1, a+2):
        for d in range(b-1, b+2):
            if (c == a and d == b) or (c < 0 or d < 0):
                continue
            try:
                k = main_list[c][d]
                count += 1 if k == 1 else 0
            except:
                pass
    return count
                

for i in range(9):
    a = [random.randint(0,1) for _ in range(9)]
    main_list.append(a)

for i in main_list:
    print(i)

i, j = map(int, input().split())

print(get_count_of_boom(i-1, j-1))

