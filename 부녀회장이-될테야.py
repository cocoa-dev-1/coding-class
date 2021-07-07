from typing import no_type_check_decorator


t = int(input())
def get_person(k, n):
    b = 0
    if k == 0:
        return n
    
    for j in range(n):
        b += get_person(k-1, j+1)
    return b
    
    

for _ in range(t):
    k = int(input())
    n = int(input())
    a = get_person(k, n)
    print(a)
    