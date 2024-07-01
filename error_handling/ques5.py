try:
    number=input(" 5 divided by?")
    number=int(number)
    print(10/number)
except ValueError as e:
    print("you have given invalid input")
    print(e)    
except ZeroDivisionError as e:
    print("you can't divide by zero")

finally:
    print("This code always run")
