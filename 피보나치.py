#r, c = map(int, input().split())

fibo_dict = {1:1, 2:1}

n = int(input())


def func1(n):
    if n in fibo_dict:
        return fibo_dict[n]
    else:
        fibo_dict[n] = func1(n-1) + func1(n-2)
        return fibo_dict[n]

f = func1(n)
print(f)