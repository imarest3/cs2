from math import pi

def perimeter(radius):
    double_pi = 2 * pi
    result = double_pi * radius
    return result

def area(radius):
    radius_squared = radius ^ 2
    result = radius_squared * pi
    return result

if __name__ == "__main__":
    print("Perimeter of a circle with radius = 10 is", perimeter(10))
    print("Area of a circle with radius = 10 is", perimeter(10))