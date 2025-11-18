class Vehicle:
    def __init__(self,Brand,Year):
        self.Brand=Brand
        self.Year=Year
    def display_info(self):
        print(f"Brand : {self.Brand}")
        print(f"Year : {self.Year}")
class Car(Vehicle):
    def __init__(self, Brand, Year,num_doors):
        super().__init__(Brand, Year)
        self.num_doors=num_doors
    def display_info(self):
        super().display_info()
        print(f"number of doors : {self.num_doors}")
class Motorcycle(Vehicle):
    def __init__(self, Brand, Year,has_sidecar):
        super().__init__(Brand, Year)
        self.has_sidecar=has_sidecar
    def display_info(self):
        super().display_info()
        print(f"has sidecar:{self.has_sidecar}")

brand1=input("please enter a Brand of Car : ")
Year1=input("please enter a year of Car : ")
doors1=input("please enter a number of doors : ")


car1=Car(brand1,Year1,doors1)


brand2=input("please enter a Brand of motor : ")
Year2=input("please enter a year of motor : ")
sidecar=input(" has a sidecar ? : ")


motor1=Motorcycle(brand2,Year2,sidecar)

car1.display_info()
print("---")
motor1.display_info()