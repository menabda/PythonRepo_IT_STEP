import csv
#იუზერის დამატება
def add_user(csv_file):
    id = input("Enter ID: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    subject_name = input("Enter Subject Name: ")
    marks = input("Enter Marks: ")

    with open(csv_file, 'a', newline='') as file:
        writer = csv.writer(file, dialect='My_dialect')
        writer.writerow([id, name, age, subject_name, marks])

def update_grade(csv_file):
    id = input("Enter ID: ")
    subject = input("Enter Subject Name: ")
    new_grade = input("Enter Marks: ")
    with open(csv_file, 'r+', newline='') as file:
        reader = csv.reader(file, delimiter='|')
        lines = list(reader)
        for line in lines:
            if line[0] == id and line[4] == subject:
                line[3] = new_grade

        file.seek(0)
        writer = csv.writer(file, dialect='My_dialect')
        writer.writerows(lines)
#ჰედერი
head = ['ID', 'Name', 'Age', 'Grade', 'Subject Name', 'Marks']

csv.register_dialect('My_dialect', delimiter='|', quoting=csv.QUOTE_NONNUMERIC)
#ჰედერის ჩაწერა(გაუშვით ერთხელ შესაქმნელად)
with open("data.csv", mode='w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file, dialect='My_dialect')
    writer.writerow(head)
#იუზერის დამატება
add_user("data.csv")
#ქულის განახლება
update_grade("data.csv")
#წაკითხვა
with open("data.csv", mode='r', encoding='utf-8') as file:
    reader = list(csv.reader(file, delimiter='|'))

    w1 = 10
    w2 = 10
    underline = 35
    count = 0

    for row in reader:
        print(f"{row[0]:<{w1}}{row[1]:<{w2}}{row[2]}{row[2]:<{w1}}{row[3]:<{w1}}{row[4]:<{w1}}")

        if count == 0:
            print('=' * underline)
            count += 1
        else:
            print('-' * underline)