class Square:
    def __init__(self, side, color):
        self.color = color
        self.side = side

    def perimeter (self):
        return self.side * 4


    def area (self):
        result = self.side **2
        return result
    

    def __eq__(self, other) :
        if isinstance(other, Square):
            return self.side == other.side and self.color == other.color
        return False
        


s = Square(10,'green')
q = Square(10,'green')


print(s.perimeter())

print(f"El perímetro del cuadrado es: {s.perimeter()}")
print(f"El perimetro del segundo cuadrado es {q.perimeter()}")
print(Square(20,'red').perimeter())
print(Square(20,'red').area())
print(f"El area del cuadrado es {s.area()}")

print(f"El color del cuadraado es {s.color}")

print ('-------------------')
print(s is q)
print(s == q)
print(str(s))