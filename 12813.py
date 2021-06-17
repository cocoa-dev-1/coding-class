
def get_and_f(a, b):
    result_str = ''
    for i in range(len(a)):
        if a[i] == '1' and b[i] == '1':
            result_str += '1'
        else:
            result_str += '0'
    return result_str

def get_or_f(a, b):
    result_str = ''
    for i in range(len(a)):
        if a[i] == '1' or b[i] == '1':
            result_str += '1'
        else:
            result_str += '0'
    return result_str

def get_else_f(a, b):
    result_str = ''
    for i in range(len(a)):
        if a[i] == '1' or b[i] == '1':
            if a[i] == '1' and b[i] == '1':
                result_str += '0'
            else:
                result_str += '1'
        else:
            result_str += '0'
    return result_str

def get_not_a_f(a, b):
    result_str = ''
    for i in a:
        if i == '1':
            result_str += '0'
        else:
            result_str += '1'
    return result_str

def get_not_b_f(a, b):
    result_str = ''
    for i in b:
        if i == '1':
            result_str += '0'
        else:
            result_str += '1'
    return result_str

a = input()
b = input()

c = get_and_f(a, b)
d = get_or_f(a, b)
e = get_else_f(a, b)
f = get_not_a_f(a, b)
g = get_not_b_f(a, b)

print('')
print(c, d, e, f, g, sep='\n')

