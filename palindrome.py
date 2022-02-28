# from mypy, typing 

# "ana"
# "Cristian"

def Is_palindrome(word: str ) -> bool:
    word = word.replace(" ","").lower()
    return word == word[::-1]


def run():
    print(Is_palindrome(10000))


if __name__ == '__main__':
    run()

