divisor, n = map(int, input().split())
first_list = list(map(int, input().split()))

main_list = [i for i in first_list if i%divisor == 0 ]
main_list.sort()
print(main_list) if len(main_list) > 0 else print([-1])