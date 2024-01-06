choice= 0
while choice!=5:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    choice = int(input("Enter choice from 1 to 5:"))
    
    if choice in range(1,4):
        x = float(input("Enter first number:"))
        y = float(input("Enter Second number:"))
        if choice == 1:
            z = x + y
            print("Addition of  ",x," and ",y," is ",z)
        elif choice == 2:
            z = x - y
            print("Subtraction of  ",x," and ",y," is ",z)
        elif choice == 3:
            z = x * y
            print("Multiplication of  ",x," and ",y," is ",z)
        else:
            z = x / y
            print("Division of  ",x," and ",y," is ",z)
    elif choice == 5:
        break
    else:
        print("Invalid choice!! Please retry")
		