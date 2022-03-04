
def decorador(func):
    def envoltura():
        print("Esto se añade a mi función original")
        func()
    return envoltura

def saludo():
    print("!hola¡")



def run():
        

    saludito = decorador(saludo)
    saludito()




if __name__ == '__main__':
    run()