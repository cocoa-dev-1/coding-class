n = int(input())
main_list = []

def print_pickture(k):
    if k == 2:
        for i in main_list:
            i = i[::-1]
            for j in i:
                print(j,end="")
            print()
    elif k == 3:
        main_list.reverse()
        for i in main_list:
            print(i)
    else:
        for i in main_list:
            print(i)

for _ in range(n):
    main_list.append(input())

k = int(input())

print_pickture(k)


