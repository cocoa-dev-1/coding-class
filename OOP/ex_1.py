class Dog:
    def __init__(self,name,id, age):
        self.name = name
        self.__id = id # __를 변수 앞에 붙이면 privite 변수가 된다.
        self.age = age
    
    def change_id(self, id):
        self.__id = id
    
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    
    def speak(self, sound):
        return f"{self.name} says {sound}"

d = Dog('lily', 1, 15)
print(d)
#print(d.speak('Hello'))