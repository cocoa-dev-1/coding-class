n = int(input())
a = 1
bee_dict = {1:1}

for i in range(1, n//6+1):
    a+=6*i
    for j in range(a):
        if j+1 in bee_dict:
            continue
        bee_dict[j+1] = i+1

print(bee_dict[n])