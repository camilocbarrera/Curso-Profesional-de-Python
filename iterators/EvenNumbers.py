class EvenNumbers:
    """ Clase que implementa un iterador de todos 
    los numeros pares hasta un máximo"""

    def __init__(self, max=None):
        self.max = max

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        if not self.max or self.num <= self.max:
            result = self.num
            self.num += 2
            return result
        else:
            raise StopIteration