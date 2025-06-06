num1 = 1
num2 = 1

print(f"{num1} \n{num2}")
for i in range(10):
    fibo = num1 + num2
    num1 = num2
    num2 = fibo
    print(fibo)