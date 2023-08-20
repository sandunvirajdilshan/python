x = int(input("Enter a number: "))
factorial = 1
if x == 0 or x == 1:
    factorial = 1
else:
    for i in range(1, x + 1):
        factorial = factorial * i
print(factorial)
