class Car():
    def __init__(self,model,colour,year):
        self.model = model
        self.colour = colour
        self.year = year
    def cardetails(self):
        print(f"{self.model}")
        print(f"{self.colour}")
        print(f"{self.year}")
Car1 = Car("Tesla Model 5","Black",2023)
Car1.cardetails()
