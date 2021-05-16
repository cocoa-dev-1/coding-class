d, k = map(int, input().split())

a, b = 1, 1
for _ in range(4, d+1):
    a, b = b, a+b
print(a)
print(b)
finish1 = 1

finish2 = 0

while True:
    finish = k - a*finish1
    if finish < 0:
        break

    elif finish % b == 0:
        finish2 = finish // b
        break

    finish1 += 1

print(finish1)
print(finish2)