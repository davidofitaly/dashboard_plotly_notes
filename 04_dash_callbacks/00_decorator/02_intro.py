def dekorator(func):

    def wrapper():
        func()
        print('Wywołanie funkcji wrapper')

    return wrapper

@dekorator
def func_2():
    print('Wywolanie funkcji func_2')

func_2()