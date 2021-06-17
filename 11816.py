x = input()
type = 0
if x[:2] == '0x':
    type = 16
elif x[0] == '0':
    type = 8
else:
    type = 10

print(int(x, type))