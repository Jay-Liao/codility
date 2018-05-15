# 1.1 For loops


def loop1():
    for i in range(0, 10):
        print(i)


def loop2():
    for i in range(10):
        print(i)


def do_factorial(n):
    """
    Example:
    We are given some positive integers n.
    Let's compute the factorial of n and assign it to the variable factorial.
    The factorial of n is n! = 1 * 2 * ... * n.
    We can obtain it by starting with a and multiplying it by all the integers form 1 to n.
    """

    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    print(factorial)


def print_triangle(n):
    """
    Example:
    Let's print triangle made of asterisks ('*') separated by spaces.
    The triangle should consist of n rows, where n is given positive integer,
    and consecutive rows should contain 1, 2, ..., n asterisks.
    For example, for n = 4 the triangle should appear as follows:
    *
    * *
    * * *
    * * * *
    """

    for i in range(0, n + 1):
        for j in range(i + 1):
            print("* ", end="", flush=True)
        print("\n")


print_triangle(2)


# 1.2 While loops

# 1.3 Looping over collections of values


