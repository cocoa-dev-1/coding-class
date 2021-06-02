n = int(input())
i = 666
count = 1

while True:
    if str(i).find('666') != -1:
        print(count, n, i)
        if count == n:
            break
        count += 1
    i += 1

print(i)