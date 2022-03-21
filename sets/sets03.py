# This example is for elimintate duplicated elements in a list object in python


def remove_duplicates(somelist):
    without_duplicates = []
    for element in somelist:
        if element not in without_duplicates:
            without_duplicates.append(element)
    return without_duplicates


def remove_duplicates_with_sets(somelist):
    return list(set(somelist))


def run():
    my_list = [1, 1, 1, 2, 3, 34, 5, 6, 66, 6, 6, ]
    print(my_list)
    print(remove_duplicates_with_sets(my_list))


if __name__ == '__main__':
    run()
