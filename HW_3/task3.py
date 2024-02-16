#1. შექმენით სია num_list [44, 23, 11, 8, 20, 56, 33, 55], in-ის გამოყენებით დაწერეთ პროგრამა რომელიც შეამოწმებს თქვენს მიერ შეტანილი რიცხვი არის თუ არა სიაში.

num_list = [44, 23, 11, 8, 20, 56, 33, 55]

a = eval(input())

if a in num_list:
    print("The number in list")
else:
    print("The number not in list")

#2. დაწერეთ პროგრამა რომელიც შეამოწმებს თქვენს მიერ შეყვანილი რიცხვის ლუწობასა და კენტობას. თუ რიცხვი ლუწია გამოიტანეთ ტექსტი 'even' თუ კენტია 'odd'.

a = eval(input())

if a%2 == 0:
    print("even")
else:
    print("odd")

#3. შექმენით ორი სტრინგის ტიპის ცვლადი st1 და st2, შეადარეთ ისინი is-ის გამოყენებით, თუ ემთხვევა გამოიტანეთ ტექსტი "Same object", წინააღმდეგ შემთხვევაში "Different object"

st1 = input()
st2 = input()

if st1 in st2:
    print("same object")
else:
    print("different object")

#4. შექმენით სია num_list [44, 23, 11, 8, 20, 56, 33, 55], შეიტანეთ რიცხვი და დაწერეთ შემდეგი პირობა:
num_list = [44, 23, 11, 8, 20, 56, 33, 55]
a = eval(input())
# თუ შეტანილი რიცხვი მეტია სიაში არსებულ მე-3 ელემენტზე და ნაკლებია ბოლო ელემენტზე გამოიტანეთ ტექსტი "More than list elements";
if(a > num_list[2] and a < num_list[-1]):
    print("More than list elements")
    # თუ შეტანილი რიცხვი უდრის სიის მე-6 ელემენტს გამოიტანეთ ტექსტი "Equal";
elif(a == num_list[5]):
    print("Equal")
    # სხვა ნებისმიერ შემთხვევაში გამოიტანეთ ტექსტი "None of the conditions were met".
else:
    print("None of the conditions were met")

