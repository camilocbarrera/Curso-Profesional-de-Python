"""Python module to check  if a number is prime :3"""

def sqrt_number(number: int) -> int:
    number = int(number**(1/2))
    return number


def is_prime(number: int) -> bool:
    if number <= 1:
        return False
# check for 2 to sqrt to number
    for i in range(2,sqrt_number(number)+1):
        if number%i == 0:
            return False

    return True


def run():
    print(is_prime(6))



if __name__ == '__main__':
    run()