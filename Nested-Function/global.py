def sayName():
    name = 'john'
    def sayGreeting():
        global name
        name = 'hana'
        print(name, ' hello')
    sayGreeting()
    print(name)

sayName()
print(name)
