#8.1
try:
    num= int(input("Enter the num"))
    result=10/num
    print("Result", result)
except ZeroDivisionError:
    print("Division by zero. invalid.")

#8.2
try:
    num=int(input("Enter an integer"))
    print("Entered ",num)
except ValueError:
    print("Invalid input.")

#8.3
try:
    num=int(input("Enter a number: "))
    result=10/num
    print("Result ", result)
except ZeroDivisionError:
    print("Division by zero is not allowed")
finally:
    print("Execution completed")


