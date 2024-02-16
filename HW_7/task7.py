#1 დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს პარამეტრად n, და გამოიტანს ფიბონაჩის n რაოდენობის მიმდევრობას.
def fibonaci(n:int) -> list:
    fib_list = []
    for i in range(n+1):
        if i==0 or i==1:
            fib_list.append(i)
        else:
            fib_list.append(fib_list[-1]+fib_list[-2])
    return fib_list        

m = eval(input("შეიყვანეთ რიცხვი"))
print(fibonaci(m))

#2 დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს პარამეტრად ორ სტრიქონს და შეამოწმებს არის თუ არა სტრიქონები ანაგრამები.
# (ანაგრამი არის სიტყვა ან შესიტყვება, რომელიც წარმოიქმნება სხვა სიტყვის ან შესიტყვების ასოების გადაადგილებით). მაგ.: race და care ანაგრამებია.
def anagram_check(word1:str, word2:str) -> bool:
    sorted_word1 = sorted(word1)
    sorted_word2 = sorted(word2)
    if sorted_word1 == sorted_word2:
        return True
    else:
        print(sorted_word1)
        return False
    
str1 = input("შეიყვანეთ პირველი სიტყვა: ")
str2 = input("შეიყვანეთ მეორე სიტყვა: ")

print(anagram_check(str1,str2))


#3 დაწერეთ პითონის ფუნქცია რომელიც მიიღებს n რიცხვს და დააბრუნებს მის ფაქტორიალს.
def factorial(n:int) -> int:
    sum = 1
    for i in range(1,n+1):
        sum = sum * i
    return sum

m = eval(input("შეიყვანეთ რიცხვი"))
print(factorial(m))

#4 დაწერეთ პითნის ფუნქცია რომელიც მიიღებს ორ პარამეტრს, პირველს სტრიქონს და მეორეს სიმბოლოს. 
# ფუნქციამ უნდა მოძებნოს სტრიქონში რამდენჯერ მეორდება პარამეტრად მიღებული სიმბოლო და დააბრუნოს მისი რაოდენობა.

def symbol_count(word: str, s: str) -> int:
    count = 0
    for char in word:
        if char == s:
            count += 1
    return count

wrd = input("შეიყვანეთ სიტყვა: ")
s = input("შეიყვანეთ სიმბოლო: ")
print(symbol_count(wrd, s))