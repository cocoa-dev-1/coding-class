#f_dic = {1:1, 2:2, 3:4}
#
#def f(n):
#    if n in f_dic:
#        return f_dic[n]
#    f_dic[n] = f(n-1) + f(n-2) + f(n-3)  
#    return f_dic[n]

f_list = [1,2,4]

def f(n):
    for _ in range(n-3):
        a = f_list[0]
        b = f_list[1]
        c = f_list[2]
        f_list[0] = b
        f_list[1] = c
        f_list[2] = (a+b+c)
    return f_list[2]


if __name__ == "__main__":
    n = int(input())
    a = f(n)
    print(a%1000)