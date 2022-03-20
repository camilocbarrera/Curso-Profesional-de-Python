from datetime import datetime

def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time -initial_time
        print("Time Elapsed: " + str(time_elapsed.total_seconds()) + " Seconds" )
    return wrapper


@execution_time
def random_func():
    for _ in range(1,100000000):
        pass
        # print(_)


@execution_time
def sum(a: int, b: int) -> int:
    # print( a + b )
    return a + b

@execution_time
def saludo(nombre='Camilo'):
    print(f'Hola {nombre}')



def run():
    saludo("Polola")
    random_func()
    x = sum(10000,10)
    print(x)

if __name__ == '__main__':
    run()