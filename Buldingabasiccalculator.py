'''num1=input("Enter first number")
num2=input("Enter second number")
result=num1+num2
print(result)'''

#output is 56.8
#because python takes everything as a string so we have to convert it into interege by using int()

'''num1=input("Enter first number")
num2=input("Enter second number")
result=int(num1)+int(num2)
print(result)'''

#now it will accepts only integer i.e whole number
# it will give error when you will insert any float number so instead of using int() use float()
#float() will accept all decimal numbers

num1=input("Enter first number")
num2=input("Enter second number")
result=float(num1)+float(num2)
print(result)