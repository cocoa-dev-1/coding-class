#t = int(input())
#
#hw_list_main = []
#
#for _ in range(t):
#    h, w, n = map(int, input().split())
#    hw_list = []
#
#    for a in range(1, w+1):
#        for b in range(1, h+1):
#            if a <10:
#                StrFormat = int('{0}0{1}'.format(b, a))
#                hw_list.append(StrFormat)
#            else:
#                StrFormat = int('{0}{1}'.format(b, a))
#                hw_list.append(StrFormat)
#    hw_list_main.append(hw_list[n-1])
#
#for i in range(t):
#    print(hw_list_main[i])

t = int(input())
t_list = []
for _ in range(t):
    h, w, n = map(int, input().split())
    a = n%h
    b = n//h
    if a == 0:
        a = h
    else:
        b += 1
    t_list.append(a*100+b)
for i in range(len(t_list)):
    print(t_list[i])


    
    
    
        