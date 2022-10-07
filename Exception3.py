import os
try:
    x = int(input("Enter the first number:"))
    y = int(input("Enter the second number:"))
    print(x1/y)
    os.remove("C:/test3.txt")

except NameError:
    print( 'NameError exception occured')

except FileNotFoundError:
    print( 'FileNotFoundError exception occured')

except ZeroDivisionError:
    print( 'ZeroDivisionError exception occured')
