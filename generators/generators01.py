from itertools import count
import time
from unittest.mock import seal

from matplotlib.pyplot import ylabel


def fibo_gen():
    n1 = 0
    n2 = 1
    counter = 0
    while True:
        if counter == 0:
            counter += 1
            yield n1
        
        elif counter == 1:
            counter += 1
            yield n2
        else:
            aux = n1 + n2
            n1 , n2  = n2, aux
            



def run():
    pass



if __name__ == "__main__":
    run()