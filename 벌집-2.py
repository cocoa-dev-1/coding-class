n = int(input())
a, count = 1, 0
while a < n:
    count += 1
    a+=6*count
print(count+1)