import collections
import time


def fibo_gen(limit: int) -> collections.Iterable:
    n1 = 0
    n2 = 1
    counter = 0
    aux = 0
    while aux <= limit:
        if counter == 0:
            counter += 1
            yield n1

        elif counter == 1:
            counter += 1
            yield n2
        else:
            aux = n1 + n2
            n1, n2 = n2, aux
            counter += 1
            yield aux


def run():
    limit = int(input(" Define a limit for Fibonacci Serie!"))
    fibonacci = fibo_gen(limit)
    for e in fibonacci:
        time.sleep(1)
        print(e)


if __name__ == '__main__':
    run()
