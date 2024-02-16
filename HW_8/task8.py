#1 შექმენით გლობალური ცვლადი int_list = [10,20,30,40] და დაწერეთ პითონის ფუნქცია,
# რომელიც მიიღებს რიცხვს პარამეტრად და გლობალურ int_list სიაში ჩაამატებს პარამეტრად მიღებულ რიცხვს.

int_list = [10,20,30,40]

def add_number(n:int):
    global int_list
    int_list.append(n)

m = eval(input("შეიყვანეთ რიცხვი: "))
add_number(m)
print(int_list)

#2 დაწერეთ პითნის ფუნქცია რომელიც პარამეტრად იღებს რიცხვების სიას (ლისტს) და აბრუნებს რიცხვების ჯამს.
# პარამეტრად უნდა მიიღოს შემდეგი სია [100, 20, 30, 50, 5323, 3321, 22, 56, 700, 90, 10].

def calculate_total(*args):
    total = sum(args)
    return total

num_list = [100, 20, 30, 50, 5323, 3321, 22, 56, 700, 90, 10]
result = calculate_total(*num_list)
print(result)

#3 შექმენით გლობალური ცვლადი gl_str = "Global" 
# და დაწერეთ პითონის ფუნქცია რომელიც ქმნის ლოკალურ ცვლადს იგივე სახელით რაც გლობალურ ცვლადს აქვს (gl_str) და აბრუნებს ლოკალური ცვლადის მნიშვნელობას

gl_str = "Global" 

def print_local():
    gl_str = "Hello World"
    print(gl_str)
    return gl_str

print_local()

#4 რეკურსიის გამოყენებით დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს ერთ პარამეტრს number
# და დააბრუნებს ციფრების ჯამს (მაგალითად თუ ფუნქციამ მიიღო რიცხვი 12345, უნდა დააბრუნოს 15. რადგან 1+2+3+4+5 უდრის 15-ს).
import math
sum = 0

def recursive_sum(n:int):
    global sum   
    sum += n%10
    
    if n >= 10: 
        n = n/10
        n = math.floor(n)      
        recursive_sum(n)

    
n = eval(input("შეიყვანეთ რიცხვი: "))
recursive_sum(n)
print ("sum:" , sum)

#5 რეკურსიის გამოყენებით დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს პარამეტრად სტრიქონს და დააბრუნებს მის შებრუნებულ (revers) სტრიქონს (მაგალითად input: Hello   Output: olleH)

def reverse(data):
    if len(data) == 0:
        return data
    else:
        return reverse(data[1:]) + data[0]

revers = input("შეიყვანეთ სიტყვა: ")

print(reverse(revers))
