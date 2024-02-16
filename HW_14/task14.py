import json
from os import getcwd


chess_players = [
  {'id': 19, 'name': 'Jobava', 'country': 'Georgia', 'rating': 2588, 'age': 41},
  {'id': 28, 'name': 'Caruana', 'country': 'USA', 'rating': 2781, 'age': 32},
  {'id': 35, 'name': 'Giri', 'country': 'Netherlands', 'rating': 2771, 'age': 30},
  {'id': 84, 'name': 'Carlsen', 'country': 'Norway', 'rating': 2864, 'age': 34},
  {'id': 118, 'name': 'Ding', 'country': 'China', 'rating': 2799, 'age': 32},
  {'id': 139, 'name': 'Karjakin', 'country': 'Russia', 'rating': 2747, 'age': 35},
  {'id': 258, 'name': 'Duda', 'country': 'Poland', 'rating': 2731, 'age': 31},
  {'id': 301, 'name': 'Vachier-Lagrave', 'country': 'France', 'rating': 2737, 'age': 34},
  {'id': 403, 'name': 'Nakamura', 'country': 'USA', 'rating': 2768, 'age': 36},
]
extension =[
  {'id': 568, 'name': 'Kasparov', 'country': 'Russia', 'rating': 2705, 'age': 56},
  {'id': 189, 'name': 'Karpov', 'country': 'Russia', 'rating': 2698, 'age': 59},
]

def write_data_into_json_file(path, json_file):
  with open(path, mode='w', encoding='utf-8') as file:
    file.write(json.dumps(json_file))

def create_json_file(path, file_name):
  file_path = f"{path}/{file_name}.json"

  try:
    file = open(file_path, mode='x', encoding='utf-8')
    file.close()
  except FileExistsError:
    print(f"File {file_path} Exists")
    print("Keep working...\n")

  # files/jsons/data1.json
  return file_path    

def read_json_file(path):
  with open(path, mode='r', encoding='utf-8') as file:
    return json.loads(file.read())
  
def update_json_file(path, json_data):
  students_list = read_json_file(path)
  students_list.append(json_data)
  write_data_into_json_file(path, students_list)

#დაწერეთ პითონის ფუნქცია რომელიც კონტექსტის მენეჯერის გამოყენებით პარამეტრად მიიღებს ფაილის მისამართს, სახელს და შემქნის მას.
file_path = create_json_file(getcwd(), "file1")
write_data_into_json_file(file_path, chess_players)

#დაწერეთ პითონის ფუნქცია რომელიც წაიკითხავს პარამეტრად მიღებული ფაილის კონტენტს
print(read_json_file(file_path))
#დაწერეთ პითონის ფუნქცია, რომელიც გაანახლებს ფაილში არსებულ კონტენტს.
data = {'id': 404, 'name': 'James', 'country': 'Armenia', 'rating': 2768, 'age': 32}
update_json_file(file_path,data)

#დაწერეთ პითონის ფუნქცია რომელიც პარამეტრად მიიღებს ლექსიკონს (dict) და ჩაწერს/გაანახლებს ფაილის კონტენტს
#ბოლოში უნდა ჩაემატოს მხოლოდ ორი ლექსიკონი და არა სია
def add_list(path, list:list):
  for dict in list:
    update_json_file(path,dict)

add_list(file_path,extension)
print(read_json_file(file_path))
