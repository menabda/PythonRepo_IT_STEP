#1. დაწერეთ პროგრამა რომელიც input მეთოდის საშუალებით მიიღებს 2 რიცხვს და დააბრუნებს ამ რიცხვებს შორის შესრულებული არითმეტიკული ოპერაციების შედეგებს (მიმატება, გამოკლება, გამრავლება, გაყოფა, ახარისხება).

a = eval(input("პირველი რიცხვი: "))
b = eval(input("მეორე რიცხვი: "))

print("ჯამია: ", a+b)
print("სხვაობაა: ", a-b)
print("ნამრავლია: ", a*b)
print("განაყოფია: ", a/b)
print("ახარისხებულია: ", a**b)

#2. დაწერეთ პროგრამა რომბის ფართობის გამოსათვლელად. მომხმარებელს კლავიატურის გამოყენებით შეაქვს ორი დიაგონალის სიგრძე.

a = eval(input("პირველი დიაგონალის სიგრძე: "))
b = eval(input("მეორე დიაგონალის სიგრძე: "))
print("ფასრთობია:", (a*b)/2)

#3. მომხმარებელის შეაქვს მეტრების რაოდენობა. დაბეჭდეთ შესაბამისი მნიშვნელობა სანტიმეტრებში, დეციმეტრებში, მილიმეტრებში, მილში.

a = int(input("პირველი რიცხვი მეტრის მნიშვნელობით: "))
print("სანტიმეტრია: ", a*100)
print("მილიმეტრია: ", a*1000)
print("დეციმეტრია :", a*10)
print("მილია: ", a/1609)

#4. დაწერეთ პროგრამა, რომელიც ითვლის სამკუთხედის ფართობს. მომხმარებელს კონსოლიდან შეყავს სამკუთხედის სიმაღლისა და ფუძის მნიშვნელობა.

a = eval(input("სიმაღლე: "))
b = eval(input("ფუძის სიგრძე: "))

print("ფართობია:",(a*b)/2)