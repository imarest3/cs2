#class SuperClass:
    # superclass bod

#class SubClass(SuperClass):
    # subclass body    

class Figure:
    def __init__(self, color):     # constructor
        self.color = color         # attribute

class Circle(Figure):
    def __init__(self, radius, color):      # constructor
        super().__init__(color)             # superclass Figure constructor method 
        self.radius = radius                # private attributes



class Rectangle(Figure):
    def __init__(self, length, width, color):    # constructor
        super().__init__(color)                  # superclass Figure’s constructor 
        self.length = length                     # private attributes
        self.width = width


class Square(Rectangle):
    def __init__(self, side, color):
        super().__init__(side, side, color)  



if __name__ == '__main__':

    my_circle = Circle(5, 'green') 
    print(my_circle.radius)
    print(my_circle.color)

    print('------------')

    my_rectangle = Rectangle(10, 5, 'blue')
    print(my_rectangle.length)
    print(my_rectangle.width)
    print(my_rectangle.color)

    print('-------- Checkcheck if a subclass inherits from a superclass we can use the issubclass function: ----------')

#To check if a subclass inherits from a superclass we can use the issubclass function:
    print('-------- To check if a subclass inherits from a superclass we can use the issubclass function:----------')
    print (issubclass(Circle, Figure))
    print (issubclass(Figure, Circle))
    print (issubclass(Circle, Rectangle))
    print (issubclass(Square, Rectangle))
    print (issubclass(Square, Figure))
    print (issubclass(Square, Circle))


# As a fun fact, in Python all classes are subclasses of the object class:
    print('------ As a fun fact, in Python all classes are subclasses of the object class: -------')
    print(issubclass(Figure, object))
    print(issubclass(Rectangle, object))
    print(issubclass(Circle, object))
    print(issubclass(Square, object))
    print(issubclass(str,object))
    print(issubclass(int,object))


    print('-----With the isistance method, we can check if an object is of a certain class. Lets see to which class an object of type Circle belongs: ------')
    my_circle = Circle(5, 'green') 
    print(isinstance(my_circle, Figure))
    print(isinstance(my_circle, Circle))
    print(isinstance(my_circle, Rectangle))
