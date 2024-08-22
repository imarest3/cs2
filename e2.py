def recursive_power(a, b):
    # complete
    if b == 0:
        return 1
    return a * recursive_power(a, b-1)
if __name__ == "__main__":
    base = int(input("Enter the base: "))
    exponent = int(input("Enter the exponent: "))
    print("Result:", recursive_power(base, exponent))
