class Car:
    def __init__ (self,brand, model, horsepower):
        self.brand = brand
        self.model = model
        self.horsepower = horsepower

    def print_car (self):
        print(f"the brand of the car {self.brand}, model {self.model} has a horsepower of {self.horsepower}")

car1 = Car("ford","fiesta", 100)
car2 = Car("honda","city", 80)
car3 = Car("mazda","mazda3", 180)

car1.print_car()
car2.print_car()
car3.print_car()
