1, 2, 3, 5, 8

def f(n):
    if n <= 1:
        return 1
    return f(n-1) + f(n-2)

if __name__ == '__main__':
    a = int(input())
    b = f(a)
    print(b)