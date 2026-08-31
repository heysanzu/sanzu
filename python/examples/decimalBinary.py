def decimalBinary(n):
    if n >= 1:
        decimalBinary(n // 2)
    print(n % 2, end='')

number = 10
print(f"Binary representation of {number} is: ", end='')
decimalBinary(number)
print()