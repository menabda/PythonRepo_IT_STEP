import json
from typing import Any, List
from random import randint

class Address:
    def __init__(self, city: str, street: str) -> None:
        self.city = city
        self.street = street


class Student:
    ROW_ID: int = 1

    def __init__(self, name: str, mark: int, address: Address) -> None:
        self.ROW_ID = Student.ROW_ID
        self.name = name
        self.mark = mark
        self.address = address

        Student.ROW_ID += 1


class ObjectEncoder(json.JSONEncoder):
    def default(self, o: Any) -> Any:
        return o.__dict__


addresses = [
    Address(city='Tbilisi', street='Saburtalo'),
    Address(city='Ozurgeti', street='Farnavaz Mefe'),
    Address(city='Tbilisi', street='Varketili 3a, 321')
]

students = [
    Student(name='Giorgi', mark=100, address=addresses[0]),
    Student(name='Luka', mark=87, address=addresses[1]),
    Student(name='Gocha', mark=79, address=addresses[2])
]

def write_in_file() -> None:
    with open('students.json', mode='w') as file:
        json.dump(students, file, cls=ObjectEncoder, indent=2)


def read_from_file():
    with open('students.json', mode='r') as file:
        return json.load(file)


def generate_grade(mark):
    if mark in range(91, 101):
        return 'A'
    elif mark in range(81, 91):
        return 'B'
    elif mark in range(71, 81):
        return 'C'
    elif mark <= 70:
        return 'D'
    else:
        return ''

# execute
if __name__ == '__main__':
    write_in_file()
    students = read_from_file()

    for st in students:
        st['grade'] = generate_grade(st['mark'])

    write_in_file()