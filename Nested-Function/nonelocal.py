def sayName():
    name = 'john'
    def sayGreeting():
        nonlocal name
        name = 'hana'
        print(name, ' hello')
    sayGreeting()
    print(name)

sayName()
