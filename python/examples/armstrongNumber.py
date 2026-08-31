from math import *

number = int(input("Enter a number:"))

result = 0
n = 0
temp = number
while temp > 0:
    lastDigit = temp % 10
    result = result + pow(lastDigit, 3)
    temp = temp // 10

if result == number:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")