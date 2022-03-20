
my_list = [1,2,3,4,5]
my_iter = iter(my_list)




def run():
    print(my_list)
    print(next(my_iter))

if __name__ == '__main__':
    run()