#1 დაწერეთ პითნის ფუნქცია, რომელიც იღებს პარამეტრად ერთი დაიგივე ზომის სიას (list) და zip ფუნქციის გამოყენებით დააჯგუფეთ სიების ელემენტები.
#params: [1, 2, 3], ['a', 'b', 'c']  
#outputs: ["(1, 'a')", "(2, 'b')", "(3, 'c')"]

list1 = [1,2,3]
list2 = ['a', 'b', 'c']

list3 = list(zip(list1,list2))
print(list3)

#2 დაწერეთ პითონის ფუნქცია, რომელიც პარამეტრად იღებს რიცხვების სიას და აბრუნებს ელემენტების ნამრავლს. ფუნქციაში გაითვალისწინეთ გამონაკლისები (Exceptions), 
#თუ მიიღეთ არასწორი ტიპის პარამეტრს (TypeError).ფუქნციის დასაწერად გამოიყენეთ lambda და functools-ის reduce მეთოდი.
#params:[1, 2, 3, 4, 5] 
#output: 120

from functools import reduce

numbers = [1, 2, 3, 4, 5]
multiply = lambda x, y: x * y if isinstance(x, (int, float)) and isinstance(y, (int, float)) else TypeError("შეიყვანეთ მხოლოდ რიცხვები")
result = reduce(multiply, numbers)
print(result) 

#3 დაწერეთ lambda ფუნქცია რომელიც იღებს მთელი რიცხვების სიას (list) და აბრუნებს მხოლოდ სიის კენტ ელემენტებს.
#params: [1, 2, 3, 4, 5, 6, 7]
#outputs: [1, 3, 5, 7]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd = lambda x : x % 2 == 1
odd_list = list(filter(odd,numbers))
print(odd_list)

#4 დაწერეთ პითნის ფუნქცია, რომელიც იღებს ორ პარამეტრს, სტრიქონების სიასა და სტრიქონს (ending). დააბრუნეთ მხოლოდ სიის ის ელემენტები რომელიც მთავრდება,
# მეორე პარამეტრად მიწოდებული სტრიქონით. გამოიყენეთ lambda და filter ფუნქცია. გაითვალისწინეთ გამონაკლისები (TypeError), თუ სხვა გამონაკლისიც აღმოჩნდა ისიც გაითვალისწინეთ.
# მინიშნება: გადაავლეთ თვალი string მეთოდებს, მონახეთ ისეთი მეთოდი, რომელიც აბრუნებს სიტყვას, რომელიც მთავრდება რაღაც სიმბოლოებით...
# params: ['hello', 'world', 'coding', 'nod'], 'ing'  
# outputs: ['coding']
list1 = ['hello', 'world', 'coding', 'nod']
str1 = "ing"

part = lambda string: str1 in string if isinstance(string, (str)) else TypeError("შეიყვანეთ მხოლოდ სტრიქონები")

list2 = list(filter(part, list1))
print(list2)