f_dic = {}

def f(r, c):
    if r == 1 or c == 1:
        return 1
    if (r,c) in f_dic:
        return f_dic[(r,c)]
    f_dic[(r,c)] = f(r-1,c) + f(r,c-1)
    return f_dic[(r,c)]


if __name__ == '__main__':
    r, c = map(int, input().split())
    a = f(r, c)
    print(a)

