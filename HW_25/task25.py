# TODO SOLID პრინციპის დაცვით შეცვალეთ კლასების იმპლემენტაცია

# Single Responsibility Principle
class Book:
    def set_details(self, title, author):
        pass
    def get_discount_price(self, discount):
        pass

#Solution

class BookDetails:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class BookPrice:
    def __init__(self, price):
        self.price = price

    def get_discount_price(self, discount):
        discounted_price = self.price - (self.price * discount / 100)
        return discounted_price


# TODO დაამატეთ  PayPal-ის გადახდების კლასი, და  Payment
# Open/Closed Principle
class Payment:
    """  გადახდის კლასი საკრედიტო ბარათით გადახდების დასამუშავებლად
    """
    def process_credit(self, amount):
        pass

#Solution

from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class process_with_card(Payment):
    def pay(self,amount):
        print(f"amount with credit card paid is: {amount}")
        

# TODO გადააკეთეთ კლასები ისე, რომ დაიცვან ლისკოვის ჩანაცვლების პრინციპი
# Liskov Substitution Principle
class Vehicle:
    def fuel_capacity(self):
        return "100 liters"

class ElectricCar(Vehicle):
    def fuel_capacity(self):
        return "Battery capacity is 100 kWh"

#Solution

class Vehicle:
    def fuel_capacity(self):
        return "100 liters"

class ElectricCar(Vehicle):
    def fuel_capacity(self):
        return "Battery capacity is 100 kWh"

def display_fuel_capacity(vehicle):
    print(f"Fuel Capacity: {vehicle.fuel_capacity()}")


# TODO შეცვალეთ იმპლემენტაცია, რადგან ყველა მოთამაშეს არ აქვს აუდიოს ან ვიდეოს მხარდაჭერა
# Interface Segregation Principle
class MultimediaPlayer:
    def play_audio(self):
        pass
    def play_video(self):
        pass

#Solution 
    
class AudioPlayer(ABC):
    @abstractmethod
    def play_audio(self):
        pass

class VideoPlayer(ABC):
    @abstractmethod
    def play_video(self):
        pass

class MultimediaPlayer(AudioPlayer, VideoPlayer):
    def play_audio(self):
        print("Playing audio...")

    def play_video(self):
        print("Playing video...")


# TODO შეცვალეთ კლასის იმპლემენტაცია, რომ დაიცვას დამოკიდებულების ინვერსიის პრინციპი.
# Dependency Inversion Principle (DIP)
class ConsoleDisplay:
    def show(self, data):
        pass

class WeatherStation:
    def report(self, display):
        display.show("Weather Data")

#Solution

class Display(ABC):
    @abstractmethod
    def show(self, data):
        pass

class ConsoleDisplay(Display):
    def show(self, data):
        print(data)

class WeatherStation:
    def __init__(self, display):
        self.display = display

    def report(self):
        self.display.show("Weather Data")
    