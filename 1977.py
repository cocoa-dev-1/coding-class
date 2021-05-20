m = int(input())
n = int(input())

result_list = []

for i in range(1, n+1):
    if i**2 >= m and i**2 <= n:
        result_list.append(i**2)
        

if result_list == []:
    print(-1)
else:
    print(sum(result_list))
    print(min(result_list))