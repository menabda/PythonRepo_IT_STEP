# 1. დაწერეთ პითონის Car (ატრიბუტები: brand, model, year) კლასი და მოახდინეთ ამ კლასისთვის __new__ და __init__ მეთოდის გადაფარვა.

# 2. Car კლასს დაუმატეთ თითეული ატრიბუტისთვის set და get ფუნქციები მათი ცვლილებებისთვის.

# 3. დაამატეთ Car კლასის set ფუნქციებში, ვალიდაციები თითოეული ატრიბუტისთვის, მაგალითად year ატრიბუტი რომ იყოს ყოველთვის ინტეგერი და ასე შემდეგ.
class Car: 

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        print("new car added")
        return instance
    
    def __init__(self,brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        
    def get_brand(self):
        return self._brand

    def set_brand(self, brand):
        if not isinstance(brand, str):
            raise ValueError("Enter String")
        self.brand = brand

    def get_model(self):
        return self._model

    def set_model(self, model):
        if not isinstance(model, str):
            raise ValueError("Enter String")
        self.model = model

    def get_year(self):
        return self.year

    def set_year(self, year):
        if not isinstance(year, int):
            raise ValueError("Enter Integer")
        self.year = year

    def __str__(self):
        return f"Car: {self.brand} {self.model} {self.year}"

car1 = Car("Toyota", "Corolla", 2022)
print(car1)
car1.set_year(2021)
print(car1)

