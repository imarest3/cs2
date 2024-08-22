
class Rectangle(Figure):
    def __init__(self, length, width, color):    # constructor
        super().__init__(color)                  # superclass Figure’s constructor 
        self.length = length    