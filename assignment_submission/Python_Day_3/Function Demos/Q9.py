def sum_all_values(*numbers): 
    current_sum = 0
    if not numbers: 
        print("No numbers provided to sum.")
        return 0 

    print("Numbers received:", numbers)
    for num in numbers:
        current_sum += num
    return current_sum

sum1 = sum_all_values(1, 2, 3)
print(f"Sum (1, 2, 3): {sum1}")

sum2 = sum_all_values(10, 20, 30, 40, 50)
print(f"Sum (10, 20, 30, 40, 50): {sum2}")

sum3 = sum_all_values(5)
print(f"Sum (5): {sum3}")

sum4 = sum_all_values() 
print(f"Sum (no arguments): {sum4}")
