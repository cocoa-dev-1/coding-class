def solution(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base
    
n = solution(int(input()), 3)
print(n)

print(int(n, 3))