inStr = input()
print(inStr)

for i in inStr:
    if i == ' ':#
        print(' ',end='')
        continue
    asc = ord(i)
    if i in ['a', 'b', 'c', 'A', 'B', 'C']:
        asc_convert = asc + 23
    else:
        asc_convert = asc - 3

    print(chr(asc_convert),end='',sep='')