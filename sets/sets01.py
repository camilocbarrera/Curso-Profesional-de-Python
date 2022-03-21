my_set = {3, 3, 6}
my_set.add(7)
my_set.update([1, 2, 5])

my_set.update((4, 7, 8))

my_set.update((4, 7, 8), {11, 4})
print(my_set)
my_set.remove(4) # It works just when the element exists in the set
print(my_set)
my_set.discard(90) # Discartd is usefull when the element doesn't exist.
print(my_set)
# my_set_empty = {}  # This is a dictionary
# print(type(my_set_empty))
# my_set_empty2 = set()
# print(type(my_set_empty2))
# my_set_two = {[1, 2], 3, 5, 6, 5}


def run():
    pass


if __name__ == '__main__':
    run()
