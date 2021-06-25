length = 64
x = int(input())
count = 0

for i in range(7):
    a = 1 << i
    if a & x != 0:
        count += 1

print(count)


count2 = 0

while x > 0:
    if x & 1 != 0:
        count2 += 1
    x >>= 1

print(count2)