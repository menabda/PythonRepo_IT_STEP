#1 დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს და აბრუნებს სტრიქონის UTF-8 დაშიფრულ ვერსიას.

str = input("შეიყვანეთ სტრიქონი: ")

utf_str = str.encode('utf-8')

print("UTF-8 დაშიფრული ტესქსტი:", utf_str)

#2 დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს. ჩამოაშორეთ ზედმეტი ინტერვალები. ყველა სიმბოლო გადაიყვანეთ პატარა ასოებში და დაუმატეთ ქვესტრიქონი 'Python'.
# თუ შეყვანილ სტრიქონში არსებობს სიტყვა "python", ჩაანაცვლეთ "Python"-ით.
#მინიშნება: ზედმეტი ინტერვალების ჩამოსაშორებელი მეთოდია .strip().

str = input("შეიყვანეთ სტრიქონი: ")

str = str.strip() #ჩამოაშორეთ ზედმეტი ინტერვალები

str = str.lower() #ყველა სიმბოლო გადაიყვანეთ პატარა ასოებში

str = str + " Python" #დაუმატეთ ქვესტრიქონი 'Python'.

if "python" in str:
    str = str.replace("python","Python")


print(str)

#3 დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს და აბრუნებს ახალ სტრიქონს, რომელიც შედგება შეყვანილი სტრიქონის პირველი ნახევრისაგან.

str = input("შეიყვანეთ სტრიქონი: ")

n = len(str) // 2

half_str = str[:n]

print(half_str)

#4 დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს. string მოდულის გამოყენებით დაწერეთ შემოწმება.
# სტრიქონი ვალიდურია მაშინ, როდესაც ის შეიცავს ერთ ციფრს და არ არის დამატებითი სიმბოლოები ('!', '~', '#', '$' და ა.შ.)

str = input("შეიყვანეთ სტრიქონი: ")
digit_valid = False 

#ციფრის შემოწმება
for char in str: 
    if char.isdigit():
        digit_valid = True
        break

if str.isalnum() and digit_valid:
    print("სტრქიონი ვალიდურია")
else:
    print("სტრიქონი არავალიდურია")


        


#5 #დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს, სტრიქონი გადაყავს ბაიტებში, ბეჭდავს მნიშვნელობას და შემდეგ კი გადაყავს ბაიტებიდან სტრიქონში და ბეჭდავს სტრიქონს.'

str = input("შეიყვანეთ სტრიქონი: ")

byt =  str.encode()
print(byt)

new_str = byt.decode()
print(new_str)