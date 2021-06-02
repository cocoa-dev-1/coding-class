n = int(input())
a = 0

def oneToN():
    global n
    global a
    a += 1
    if a == n:
        print(a)
    else:
        print(a)
        oneToN()

oneToN()
