

n, k = map(int, input().split())
main_str = ''

for i in range(0, n*2):
    if len(main_str) >= n*5:
        break
    main_str += bin(i)[2:]
print(main_str)
print(' '.join(main_str[k-1::n]))