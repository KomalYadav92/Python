# To handle the errors
'''
number=int(input("Enter a number: "))
print(number)
'''
# here if in the output i am going to write any alphabates it will give the error
# so to handle this we can use tryexcept

# to handle this
'''
try:
    number = int(input("Enter a number: "))
    print(number)
except:
    print("Invalid number")
'''
'''
try:
    a=10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError:
    print("Division by zero")
except TypeError:
    print("Invalid input")
'''

try:
    a=10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except TypeError:
    print("Invalid input")