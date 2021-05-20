while True:
    t = input()
    if t != 'exit':
        print(t)
    else:
        break


math_score = [80, 79, 65, 100, 32]
a = 0

for i in math_score:
    a += i

print(a)
print(a/len(math_score))

b = 0

for i in math_score:
    if i > a/len(math_score) :
        b += 1

print(b)