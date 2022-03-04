
def normalice_word_decorator(func):
    def normalice_word_wrapper(word) :
        word = func(word).replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u')
        return word
    return normalice_word_wrapper



@normalice_word_decorator
def mensaje(nombre):
    return f'{nombre}, recibiste mensaje!'



def run():
    print(mensaje("Caáé"))
    

if __name__ == '__main__':
    run()