x = int(input())
y = 0
count = 0

while True:
    a = 0
    for i in str(x):
        a += int(i)
    y = a
    x = y
    count += 1
    if len(str(y)) == 1:
        break

print(count)
if x % 3 == 0:
    print('YES')
else:
    print('NO')