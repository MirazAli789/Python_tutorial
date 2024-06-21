# try-except block is used for exception handling
# try:
#     a = int(input("Enter a number\n"))
#     print(a+3)
# except Exception as e:
#     print(e)
#     print("Please enter an integer")

# try:
#     x = int(input("Enter 1st number\n"))
#     y = int(input("Enter 2nd number\n"))
#     print(x/y)
# except Exception as e:
#     print(e)
#     print("Divide by zero exception occur")

arr = [1,14,142,56,3,534]
try:
    print(arr[10])

except Exception as e:
    print(e)
    print("Array index out of bound exception")