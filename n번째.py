
n_dic = {1: 1}

def f(n):
    if n in n_dic:
        return n_dic[n]
    else:
        n_dic[n] = f(n-1)*2+1
        return n_dic[n]

if __name__=='main':
    n = int(input())

    a = f(n)
    print(a)