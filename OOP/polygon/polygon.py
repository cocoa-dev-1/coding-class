class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]
    
    def __str__(self):
        if self.sides[0] != 0:
            sides_list = ['side '+str(i+1)+': '+self.sides[i]+'' for i in range(self.n)]
            return f"length of all sides:{''.join(sides_list)}\nlength of circumference:{sum(self.sides)}\n"
        else:
            return 'the side is empty'
    
    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]
    
    def dispSides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])
    

class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 3)
    
    def __str__(self):
        a, b, c = self.sides
        # calculate the semi-perimeter
        s = (a + b + c) / 2
        area = (s* (s-a) * (s-b) * (s-c)) ** 0.5
        if self.sides[0] != 0:
            sides_list = ['side '+str(i+1)+': '+str(self.sides[i])+'' for i in range(self.n)]
            return f"length of all sides: {' '.join(sides_list)}\nlength of circumference: {sum(self.sides)}\narea: {area}"
        else:
            return 'the side is empty'
    
    def findArea(self):
        a, b, c = self.sides
        # calculate the semi-perimeter
        s = (a + b + c) / 2
        area = (s* (s-a) * (s-b) * (s-c)) ** 0.5
        print('The area of the triangle is %0.2f' %area)

class Square(Polygon):
    def __init__(self):
        Polygon.__init__(self, 4)

    def __str__(self):
        a, b, c, d = self.sides
        area = a * b
        if self.sides[0] != 0:
            sides_list = ['side '+str(i+1)+': '+str(self.sides[i])+'' for i in range(self.n)]
            return f"length of all sides: {' '.join(sides_list)}\nlength of circumference: {sum(self.sides)}\narea: {area}"
        else:
            return 'the side is empty'
    
    def findArea(self):
        a, b, c, d = self.sides
        area = a * b
        print('The area of the square is %0.2f' %area)

class Rhombus(Polygon):
    def __init__(self):
        Polygon.__init__(self, 4)

    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]
        self.hight = [float(input('Enter diagonal '+str(i+1)+' : ')) for i in range(2)]

    def findArea(self):
        a, b, c, d = self.sides
        diagonal, diagonal2 = self.hight
        area = (diagonal * diagonal2) / 2
        print('The area of the triangle is %0.2f' %area)
    
    def __str__(self):
        a, b, c, d = self.sides
        diagonal, diagonal2 = self.hight
        area = (diagonal * diagonal2) / 2
        if self.sides[0] != 0:
            sides_list = ['side '+str(i+1)+': '+str(self.sides[i])+'' for i in range(self.n)]
            return f"length of all sides: {' '.join(sides_list)}\nlength of circumference: {sum(self.sides)}\narea: {area}"
        else:
            return 'the side is empty'

t = Triangle()
t.inputSides()
t.dispSides()
t.findArea()

s = Square()
s.inputSides()
s.dispSides()
s.findArea()
print(s)

r = Rhombus()
r.inputSides()
r.dispSides()
r.findArea()
print(r)