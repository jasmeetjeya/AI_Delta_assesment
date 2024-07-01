
def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y==0:
        return "Cannot divide by zero"
    else:
        return x / y

def Simple_calculator():
    print("Simple Calculator")
    number1 = float(input("Input the first number: "))
    number2 = float(input("Input the second number: "))
   
    operations = {
        '+': addition,
        '-': subtraction,
        '*': multiplication,
        '/': division
    }

    operation = input("Enter an operation (+, -, *, /): ").strip()

    if operation in operations:
        result = operations[operation](number1, number2)
        if result is not None:
            print(f"{number1} {operation} {number2} = {result}.")
    else:
        print("Invalid Input , PLease Enter the Specified Input")

Simple_calculator()
