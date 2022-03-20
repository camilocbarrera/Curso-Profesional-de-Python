def my_gen():
    """This is an example of generators
    """
    print("Hello World!")
    n = 0
    yield n  #This keyword is similar to return, except that this doesn't finish the function, 
    
    print("hello heave!")
    n = 1
    yield n

    print("Hello hell")
    n = 2
    yield n


def run ():
    my_list = [0, 1, 4, 7, 9, 10]
    my_second_list = [x*2 for x in my_list] #List comprenhension
    my_gen_list = (x*2 for x in my_list) #Generator expresion
    



    a = my_gen()
    print(next(a))
    print(next(a))
    print(next(a))
    # print(next(a)) StopIteration


if __name__ == '__main__':
    run()