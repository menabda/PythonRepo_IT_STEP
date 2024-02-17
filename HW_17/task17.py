
class Car: 

    def __init__(self,mark, model, age):
        self.mark = mark
        self.model = model
        self.age = age

    def car_info(self):
        print(f"mark:{self.mark}, mode:{self.model}, age:{self.age}")

    def age_of_car(self):
        return 2023 - int(self.age)
        

#1. შექმენით პითონის კლასი Car, ატრიბუტებით ბრენდით, მოდელით და წლით. ასევე, შექმენით კლასის მეთოდი car_info(), რომელიც დაბეჭდავს ატრიბუტების ინფორმაციას.
        
c1 = Car("Mercedes","C class","2000")
c1.car_info()

#2. Car კლასში დაამატეთ მეთოდი age_of_car, რომელიც დაითვლის მანქანის ასაკს.
print("Age is",c1.age_of_car())

#3. შექმენით კლასი ElectricCar, რომელიც მემკვიდრეობით მიიღებს Car class-ს. დაამატეთ ახალი ატრიბუტი battery_life და მეთოდი battery_info(), რომელიც დაბეჭდავს შემდეგ სტრიქონს "ამ მანქანის ბატარეის ხანგრძლივობა არის [battery_life] საათი".
class ElectricCar(Car):

    def __init__(self, mark, model, age, battery_life):
        super().__init__(mark, model, age)
        self.battery_life = battery_life

    def battery_info(self):
        print(f"ამ მანქანის ბატარეის ხანგრძლივობა არის {self.battery_life} საათი")
        
        
c1 = ElectricCar("BMW","Z4","2020","100")
c1.battery_info()

#4. დაამატეთ Car კლასს ატრიბუტი number_of_cars, რომელიც დაითვლის მანქანების სრულ რაოდენობას. გაზარდეთ ეს ცვლადი ყოველ ჯერზე, მანქანის შექმნისას. 
class Car: 
    number_of_cars = 0

    def __init__(self,mark, model, age):
        self.mark = mark
        self.model = model
        self.age = age
        Car.number_of_cars += 1

    def car_info(self):
        print(f"mark:{self.mark}, mode:{self.model}, age:{self.age}")

    def age_of_car(self):
        return 2023 - int(self.age)
    
car1 = Car("Toyota", "Camry", "2015")
car2 = Car("Tesla", "Model S", "2020")
car3 = Car("Ford", "Focus", "2018")

print(Car.number_of_cars)


#5. Car კლასს დაამატეთ მეთოდი total_cars(), რომელიც გამოიტანს მანქანების მთლიან რაოდენობას.
class Car: 
    number_of_cars = 0

    def __init__(self,mark, model, age):
        self.mark = mark
        self.model = model
        self.age = age
        Car.number_of_cars += 1

    def car_info(self):
        print(f"mark:{self.mark}, mode:{self.model}, age:{self.age}")

    def age_of_car(self):
        return 2023 - int(self.age)
    
    def total_cars(self):
        print(self.number_of_cars)
    
car1 = Car("Toyota", "Camry", "2015")
car2 = Car("Tesla", "Model S", "2020")
car3 = Car("Ford", "Focus", "2018")

car1.total_cars()