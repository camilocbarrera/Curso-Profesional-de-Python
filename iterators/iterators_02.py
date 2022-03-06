

#Creating iterator
my_list = [1,2,3,4,5]
my_iter = iter(my_list)

# print(next(my_list))

#Itering interator
while True:
    try:
        element = next(my_iter)
        print(element)
    except StopIteration:
        break


def run():
    pass

if __name__ == '__main__':
    run()