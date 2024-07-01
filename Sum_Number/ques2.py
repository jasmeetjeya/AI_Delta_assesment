def sum_number():
    string_input = input("Enter the numbers for sum, separated by spaces: ")
    string_list = string_input.split()
    numbers = [int(num) for num in string_list]
    total = sum(numbers)
    
    return total

print("The sum of the number is:",sum_number())
