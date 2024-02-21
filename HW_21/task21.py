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
        self.name = name
        self.mark = mark
        self.address = address


class ObjectEncoder(json.JSONEncoder):
    def default(self, o: Any) -> Any:
        attrs_dict = o.__dict__
        row_id = 'ROW_ID'
        print(hasattr(o, row_id))
        if hasattr(o, row_id):
            attrs_dict[row_id] = getattr(o, row_id)

        print(attrs_dict)
        return attrs_dict


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
    with open('students.json', mode='a') as file:
        file.write(json.dumps(students, cls=ObjectEncoder))


def read_from_file() -> List[Address]:
    with open('students.json', mode='r') as file:
        print(json.loads(file.read()))


def convert_to_objects(serialized_data) -> List[Student]:
    students = []
    for student in serialized_data:
        address = Address(**student.get('address'))
        students.append(Student(
            address=address,
            name=student.get('name'),
            mark=student.get('mark')
        ))

    return student

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

    for student in students:
        student.mark = randint(0, 101)
        student.grade = generate_grade(student.mark)