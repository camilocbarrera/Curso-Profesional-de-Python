def decorador(func):
    def envoltura():
        print("Esto se ageraga a mi función original")
        func()
    return envoltura

@decorador
def saludo():
    print("¡Hola!")




def run():
    saludo()

if __name__ == '__main__':
    run()