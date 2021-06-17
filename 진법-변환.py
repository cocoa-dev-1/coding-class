

# def get_result(k, v):
#     return_data = ''
#     while k > 0:
#         i = k%v
#         k = k//v
#         return_data += str(i)
#         print(k, i)
#     return return_data[::-1]
def get_result(k, v):
    a = 0
    b = 0
    for i in range(k):
        a+= 1
        b+= 1
        if str(v) in str(b):
            b = up_count(b, v)
            # print(b)
        print(a, b)
            #print(b)
    return a, b
        
def up_count(k, v):
    if str(v) in str(k):
        c = str(k).rfind(str(v))
        c = len(str(k)) - c
        k = (k//(10**c))*(10**c)
        k += 10**c
        if c == 0 and len(str(k)) == 1:
            k = 10
        print(k, c)
        if str(v) in str(k):
            return up_count(k, v)
        else:
            return k


            

if __name__ == "__main__":
    a = int(input())
    b = int(input())
    c, d = get_result(a, b)
    print(c, d)
    print(c, int(str(d), b))
