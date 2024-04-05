# #1. დაწერეთ პროგრამა, რომელიც ქმნის ორ ძაფს (Thread) 30-დან 50-ის ჩათვლით ლუწი და კენტი რიცხვების მოსაძებნად. შედეგი დაბეჭდეთ ეკრანზე

import threading

def is_even(num):
    return num % 2 == 0

def is_odd(num):
    return num % 2 == 1 

def find_even_numbers(start, end):
    even_numbers = []
    for num in range(start, end + 1):
        if is_even(num):
            even_numbers.append(num)
    print(f"Even numbers between {start} and {end}: {even_numbers}")

def find_odd_numbers(start, end):
    odd_numbers = []
    for num in range(start, end + 1):
        if is_odd(num):
            odd_numbers.append(num)
    print(f"Even numbers between {start} and {end}: {odd_numbers}")

def filter_numbers(start, end):
    find_odd_numbers(start, end)
    find_even_numbers(start, end)

thread1 = threading.Thread(target=filter_numbers, args=(30, 39))
thread2 = threading.Thread(target=filter_numbers, args=(40, 50))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Both threads finished.")



#2. დაწერეთ პროგრამა, რომელიც ქმნის რამდენიმე ძაფს (Thread) და იწერს რამდენიმე mp3 ფაილს ინტერნეტიდან.

import threading
import requests


def download_mp3(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as music:
            music.write(response.content)
        print(f"Downloaded {filename}")
    else:
        print(f"Failed to download {filename}")

url1 = "https://onlinetestcase.com/wp-content/uploads/2023/06/100-KB-MP3.mp3"
url2 = "https://onlinetestcase.com/wp-content/uploads/2023/06/500-KB-MP3.mp3"

thread1 = threading.Thread(target=download_mp3, args=(url1, "100-KB-MP3.mp3"))
thread2 = threading.Thread(target=download_mp3, args=(url2, "500-KB-MP3.mp3"))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Both downloads finished.")
