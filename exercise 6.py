class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Year: {self.year}")


class Car(Vehicle):
    def __init__(self, brand, year, num_doors):
        super().__init__(brand, year)
        self.num_doors = num_doors

    def display_info(self):
        super().display_info()
        print(f"Number of Doors: {self.num_doors}")


class Motorcycle(Vehicle):
    def __init__(self, brand, year, has_sidecar):
        super().__init__(brand, year)
        self.has_sidecar = has_sidecar

    def display_info(self):
        super().display_info()
        print(f"Has Sidecar: {self.has_sidecar}")


# Creating objects and calling display_info
car1 = Car("Toyota", 2020, 4)
motor1 = Motorcycle("Honda", 2018, True)

car1.display_info()
print("---")
motor1.display_info()
