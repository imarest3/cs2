def int_div(a, b):
    #Complete
    if a < b:
        return 0
    return 1+ int_div(a-b,b)
if __name__ == "__main__":
    dividend = int(input("Enter the dividend: "))
    divisor = int(input("Enter the divisor: "))
    print("Result:", int_div(dividend, divisor))
