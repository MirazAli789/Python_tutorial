# simple calculator
print()
print("calculator * - + /\n")
a = int(input("Enter a number\n"))
b = int(input("Enter another number\n"))
desc = int(
    input(
        "Enter 1 for addition \nEnter 2 for subtraction \nEnter 3 for multiplication \nEnter 4 for division\nEnter 5 for modulo \nEnter 6 for exponential\n"
    )
)
match (desc):
    case 1:
        print(a, " + ", b, " = ", a + b)
    case 2:
        print(a, " - ", b, " = ", a - b)
    case 3:
        print(a, " * ", b, " = ", a * b)
    case 4:
        print(a, " / ", b, " = ", a // b)
    case 5:
        print(a, " % ", b, " = ", a % b)
    case 6:
        print(a, " ^ ", b, " = ", a**b)
    case _:
        print("default")
