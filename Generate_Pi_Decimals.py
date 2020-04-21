import math, os
from decimal import Decimal, getcontext
from IPython.display import clear_output
getcontext().prec = 1000


def calc_pi(n):
    """
    This is where pi is calculated
    :param n: number of loop for the Chudnovsky algorithm(The higher, the longer time it takes and more precise
    :return: a default pi used for the whole program
    """
    result = Decimal(0)
    for a in range(n):
        above = Decimal(math.factorial(6 * a) * (545140134 * a + 13591409))
        below = Decimal(math.factorial(3 * a) * math.factorial(a) ** 3 * (-262537412640768000) ** a)
        temp = Decimal(above / below)
        result += Decimal(temp)
    return Decimal(426880) * Decimal(math.sqrt(10005)) / Decimal(result)


def generate_pi(n, p):
    """

    :param n: number of decimal you after the ',' you want to generate
    :param p: the calculated pi
    :return: the correct pi
    """
    a = p
    a = round(p, n)

    if a - p > 0:
        a = a - 1 / (10 ** n)
        a = round(a, n)

    return print(a)


def exe():
    """
    This is where the program execute.
    :return: the desired pi
    """
    print("Initializing the pi number, it will only take a moment.")
    a = Decimal(calc_pi(1000))
    os.system("cls")
    #clear_output()
    number_of_decimal = int(input("Please enter the number of decimal you want to generate: "))
    print(f"Here is your pi with {number_of_decimal} decimal after the '.'")
    generate_pi(number_of_decimal, a)

if __name__ == "__main__":
    exe()