num1 = int(input("Enter the number: "))
num2 = int(input("Enter the number: "))
operator = input("Enter the operator (+, -, *, /): ")

if operator == "+":
    result = num1 + num2
    print(f"result: {result}")

elif operator == "-":
    result = num1 - num2
    print(f"result: {result}")

elif operator == "*":
    result = num1 * num2
    print(f"result: {result}")

elif operator == "/":
    if num2 != 0:  # error handling
        result = num1 / num2
        print(f"result: {result}")
    else:
        print("Error: Cannot divide by zero")

else:
    print("Invalid operator")