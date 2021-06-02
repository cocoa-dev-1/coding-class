import random
rand_nums = [random.randint(0,10) for _ in range(10)]

print(rand_nums)

p = [1, 2, 3, 4, 5, 6, 7]

for i in range(len(rand_nums)):
    print(rand_nums[i], p[i%len(p)])