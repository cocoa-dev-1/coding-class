n = input()

a_to_z = [chr(i) for i in range(97, 123)]
main_list = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]

def get_count(x,y):
    x = a_to_z.index(x) +1
    count = 0
    for i in main_list:
        nx = x + i[0]
        ny = y + i[1]
        if nx > 0 and ny > 0 and nx <= 8 and ny <= 8:
            count += 1
    return count


a = get_count(n[0], int(n[1]))
print(a)

