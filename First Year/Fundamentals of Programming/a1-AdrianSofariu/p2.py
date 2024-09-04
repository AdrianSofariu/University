# Solve the problem from the second set here
"""

8. Find the smallest number m from the Fibonacci sequence, defined by f[0]=f[1]=1, f[n]=f[n-1] + f[n-2], for n > 2,
larger than the given natural number n. (e.g. for n = 6, m = 8).

"""


def fibonacci(nr: int) -> int:
    fibo0, fibo1 = 1, 1
    while fibo0 <= nr:
        fibo2 = fibo0 + fibo1
        fibo0 = fibo1
        fibo1 = fibo2
    return fibo0


def print_menu():
    while True:
        nr_string = input("Choose a number:\n")
        if nr_string == "exit":
            break
        else:
            try:
                nr = int(nr_string)
                result = fibonacci(nr)
                print(result)
            except ValueError:
                print("Please choose a valid number")


if __name__ == "__main__":

    print("This program finds the smallest number from the Fibonacci sequence bigger than a chosen number."
          "To exit type 'exit'")
    print_menu()
