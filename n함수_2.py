n = int(input())
a = 0
count = 1

def one_to_n(b):
    global count
    global a
    global n
    a += b
    count += 1
    if count > n:
        print(a)
    else:
        one_to_n(count)

one_to_n(1)