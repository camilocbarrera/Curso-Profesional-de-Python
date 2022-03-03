""" This closure retuns a function that returns the division of
        an x number by n
    """
def make_division_by(n):
    def times_division(x):
        return x/n
    return times_division




def run ():

    div_10 = make_division_by(3)
    print(div_10(18))

    div_10 = make_division_by(5)
    print(div_10(100))

    div_10 = make_division_by(18)
    print(div_10(54))
    

if __name__ == '__main__':
    run()