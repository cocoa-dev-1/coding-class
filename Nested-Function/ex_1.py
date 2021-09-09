def sayName():
    name = 'john'
    print('sayName ', name)
    def sayGreeting():
        nonlocal name
        name = 'hana'
        #name = 'hana'
        print('sayGreeting ', name, ' hello')
        def sayGreeting2():
            nonlocal name
            #name = 'jin'
            print('sayGreeting2 ', name, ' bye')
        sayGreeting2()
    sayGreeting()

sayName()
