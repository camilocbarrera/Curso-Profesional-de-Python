"""
This example represents the sense of a close
Not how in the main method wi can declare a variable 
with the firts beahavior of the multiply_str function

"""

def repiter(string_p):
    assert type(string_p) == str, "Just it's posible use strings"
    def make_repiter_of(n):
        
        return string_p * n 
        
    return make_repiter_of


def run():

    name = repiter("hola")
    name(4)

    print(name(4))


if __name__ == '__main__':
    run()