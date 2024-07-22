class Car:
    def __init__(self, brand, model, horsepower):
        self.brand = brand
        self.model = model
        self.horsepower = horsepower

    def print_car(self):
        print(f"The car of brand {self.brand}, model {self.model} has a horsepower of {self.horsepower}.")


if __name__ == "__main__":
    car1 = Car("Ford", "Focus", 90)
    car2 = Car("Toyota", "Corolla", 120)
    car3 = Car("Honda", "Civic", 150)

    car1.print_car()
    car2.print_car()
    car3.print_car()