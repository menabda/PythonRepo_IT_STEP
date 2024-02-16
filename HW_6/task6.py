#1 დაწერეთ პითონის პროგრამა, რომელიც დასაწყისში შექმნის ცარიელ სიას ([]), თუ მომხარებელი შეიყვანს სიმბოლო 'a'-ს, ნიშნავს რომ უნდა დაამატოთ სიაში რიცხვი; თუ აკრიფა 'r', სიიდან უნა წაიშალოს რიცხვი; 'e'-ს შეტანისას პროგრამამ უნდა დაასრულოს მუშაობა. მიღებული შედეგი დაბეჭდეთ კონსოლში.
# მომხარებელმა უნდა შეიყვანოს შემდეგი სტრუქტურით ბრძანება "{command} {number}" commands:
# a – append
# r – remove
# e – exit
# მხოლოდ გამოიყენეთ ეს ბრძანებები და მოახდინეთ სიაზე ზემოქმედება

numbers = []

while(True):
    command = input("შეიყვანეთ ბრძანება: ")
    if command == "e":
        break
    elif command == "a":
        number = input("შეიყვანეთ რიცხვი: ")
        number = int(number)
        numbers.append(number)
        print("მიმდინარე ელემენტები: ", numbers)
    elif command == "r":
        number = input("შეიყვანეთ რიცხვი: ")
        number = int(number)
        numbers.remove(number)
        print("მიმდინარე ელემენტები: ", numbers)
    else:
        print("არასწორი ბრძანება")

print("საბოლოო ელემენტები: ", numbers)

#2 დაწერეთ პითონის პროგრამა, რომელიც შექმნის სიას my_list = [43, '22', 12, 66, 210, ["hi"], და შეასრულებს შემდეგ ნაბიჯებს:
my_list = [43, '22', 12, 66, 210, ["hi"]]
# a. დაბეჭდავს 210-ის ინდექსს;
print(my_list.index(210))

# b. დაამატებს ბოლო ელემენტში ტექსტს "hello";
my_list[-1].append("hello")

# c. წაშლის მეორე ინდექსზე მდგომ ელემენტს და დაბეჭდავს სიას;
my_list.pop(2)
print(my_list)

# d. შექმენით ახალი სია my_llist_2, რომელსაც ექნება my_llist-ის მნიშვნელობა, გაასუფთავეთ my_llist_2-ის მნიშნველობა და დაბეჭდეთ ორივე სია.
my_list_2 = my_list.copy()
my_list_2.clear()
print(my_list, my_list_2)

#3 დაწერეთ პითნის პროგრამა, რომელიც მიიღებს ტელეფონის ნომერს და regex-ით შეამოწმებს შეყვანილი ნომერი იცავს თუ არა "(123) 456-789" ფორმატს, 
#თუ იცავს დააბრუნეთ შეყნვაილი ტელეფონის ნომერი, წინააღმდეგ შემთხვევაში გამოიტანეთ "Invalid format" ტექსტი.

import re

pattern = r'\(\d{3}\) \d{3}-\d{3}'
number = input("შეიყვანეთ რიცხვი: ")

match = re.match(pattern, number)
if match:
    print(number)
else:
    print("Invalid format")