#find even in range


def print_even(a, b):
    for i in range(a, b + 1):
        if i % 2 == 0:
            print(i)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print_even(a, b)

