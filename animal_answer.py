# implement the class Animal
class Animal:
    def __init__ (self, name, weight, age):
        self.name = name
        self.weight = weight
        self.age = age
    def __str__(self):
        return f"Name: {self.name}, Weight: {self.weight}, Age: {self.age}"




# implement the class Dog as a subclass of Animal
class Dog(Animal):
    def __init__(self,name, weight, age, color, breed):
        super().__init__(name, weight, age)
        self.color = color
        self.breed = breed

    def bite(self):
        print(f'{self.name} bites')

    def __str__(self):
        return f"{super().__str__()}, Color: {self.color}, Breed: {self.breed}"


# implement the class Chicken as a subclass of Animal





def main():
    # provide an example using the to_list method
    animal = Animal("Animal comun", 50, 5)
    print(animal)

    dog = Dog("Toño", 20, 3, "Brown", "Labrador")
    print(dog)
    dog.bite()



if __name__ == "__main__":
    main()