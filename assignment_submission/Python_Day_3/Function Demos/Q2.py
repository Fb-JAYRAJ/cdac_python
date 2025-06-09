def calculate_square(number):
    return number * number

num_for_square = int(input("Enter a number to get its square: "))
squared_value = calculate_square(num_for_square)
print(f"The square of {num_for_square} is {squared_value}.")

def display_values(char_val, int_val, str_val):
    print(f"Character: {char_val}")
    print(f"Integer: {int_val}")
    print(f"String: {str_val}")
