
t = int(input())

for _ in range(t):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    main_list = []
    count = 0
    for _ in range(n):
        cx, cy, r = map(int, input().split())
        circle_list = []
        circle_list.append(int(((cx-x1)**2 + (cy-y1)**2)**0.5))
        circle_list.append(int(((cx-x2)**2 + (cy-y2)**2)**0.5))
        for i in circle_list:
            if i < r:
                count += 1
    print(count)
