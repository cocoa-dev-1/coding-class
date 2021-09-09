def square(x):
    return x * x

def cube(x):
    return x * x * x

def quad(x):
    return x * x * x * x

def my_map(func, args):
    res = []
    for i in args:
        res.append(func(i))
    
    return res

lst = [1,2,3,4,5]

squares = my_map(square, lst)
cubes = my_map(cube, lst)
quads = my_map(quad, lst)

print(squares)
print(cubes)
print(quads)