def squre(x):
    return x * x

print(squre(5))

f = squre

print(f)
print(f(5))

def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

func_list = [add, substract, multiply, divide]
a = int(input('a의 값을 입력하세요: '))
b = int(input('b의 값을 입력하세요: '))

for func in func_list:
    print(func.__name__, ':', func(a, b))