def binaryDecimal(n):
    if len(n) == 0:
        return 0
    return int(n[-1]) + 2 * binaryDecimal(n[:-1])

binary = "01010"
print(f"Decimal representation of {binary} is: {binaryDecimal(binary)}")