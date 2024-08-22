class Square:
    def __init__(self, side, color):   #constructor
        self.__color = color        #private attributtes
        self.__side = side          

    def get_color (self):           #getter method for __color
        return self.__color
    
    def set_color (self, color):    #setter method for __color
        self.__color = color

    def get_side(self):             #getter method for __side
        return self.__side
    
    def set_side(self, side):
        if type (side) is int and side > 0:       # setter method for __side​
            self.__side = side


    def __eq__(self, other) :
        if isinstance(other, Square):
            return self.__side == other.__side and self.__color == other.__color
        return False
    
    def __str__(self):                 # will be called with str(square_instance)
        return '(' + self.__color + ', ' + str(self.__side) + ')' 



s = Square(10,'green')   # creates a green square of side 10​
print(s.get_side())      # using the get method to reed the side​
s.set_side(7)            # using the set method to modify the side​
print(s.get_side()) 

q = Square(10, 'green')
q.set_side(7)

print(s is q)
print(s == q)
print(str(s))

print(s._Square__color)