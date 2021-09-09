def cal_parimeter():
    pi = 3.14156
    def circle_perimeter(radius):
        return 2*radius*pi
    return circle_perimeter

c = cal_parimeter()

print(c(1), c(2), c(3), c(4), c(5))