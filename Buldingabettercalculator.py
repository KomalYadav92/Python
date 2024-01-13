num1=input("Enter first Number")
num2=input("Enter second Number")
op=input("Enter the operator (+,-,*,/)")

if op=='+':
    result=float(num1)+float(num2)
    print(result)

elif op=='-':
    result = float(num1) -float(num2)
    print(result)

elif op == '*':
    result = float(num1) * float(num2)
    print(result)

elif op == '/':
    result = float(num1) / float(num2)
    print(result)

else:
    print("Invalid operator")