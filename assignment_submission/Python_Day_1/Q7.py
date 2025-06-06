total = 0

while True:
    num = int(input("Enter the number: "))
    if num == 0:
        break
    total += num

print("Total of all numbers entered:", total)