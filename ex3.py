testString = 'ooxxooxxoo'
a = 0
b = 0
for i in testString:
    if i == 'o':
        a += 1+b
        b += 1
        print(a)
    else:
        b = 0
        

print(a)