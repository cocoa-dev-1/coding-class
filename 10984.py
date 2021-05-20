
T = int(input())

Tinfo_main_list = []
Tresult_main_list = []

Tinfo_main = 0
Tresult_main = 0.0

for a in range(T):
    n = int(input())
    Tinfo_list = []
    Tresult_list = []

    for b in range(n):
        c, g = input().split()
        c = int(c)
        g = float(g)
        Tinfo_list.append(c)
        Tresult_list.append(c*g)

    Tinfo_main_list.append(Tinfo_list)
    Tresult_main_list.append(Tresult_list)

for i in range(len(Tinfo_main_list)):
    Tinfo_main = sum(Tinfo_main_list[i])
    Tresult_main = float('{0:0.1f}'.format(sum(Tresult_main_list[i]) / Tinfo_main))  
    print(Tinfo_main, Tresult_main)

