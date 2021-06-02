a, b = map(int, input().split())
main_count = []

def get_gen(num):
    count = 0
    while True:
        count += 1
        result = count
        for i in str(count):
            result += int(i)
        if result == num:
            return True
        elif result > num:
            return False

for i in range(a, b+1):
    a = get_gen(i)
    print(a, i)
    if a == False:
        main_count.append(i)

print(sum(main_count))
