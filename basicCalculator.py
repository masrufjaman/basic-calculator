print("Choose Operation:")
print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVISION")

operation = input()

if operation == "1":
    # !code for addition
    num2 = input("Enter another number: ")
    num1 = input("Enter a number: ")

    print("The Sum is: " + str(int(num1) + int(num2)))
elif operation == "2":
    # !code for substraction
    num1 = input("Enter a number: ")
    num2 = input("Enter another number: ")

    print("The Difference is: " + str(int(num1) - int(num2)))
elif operation == "3":
    # !code for multiplication
    num1 = input("Enter a number: ")
    num2 = input("Enter another number: ")

    print("The Product is: " + str(int(num1) * int(num2)))
elif operation == "4":
    # !code for division
    num1 = input("Enter a number: ")
    num2 = input("Enter another number: ")

    print("The Result is: " + str(int(num1) / int(num2)))
else:
    print("Invalid Operation Choice!")
