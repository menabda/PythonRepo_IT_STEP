# 1. შექმენით ვექტორის Vector კლასი, რომელიც წარმოადგენს 2D ვექტორს. კლასს უნდა ჰქონდეს ორი ატრიბუტი x და y. კლასში დაამატეთ __add__ მეთოდი, რომ მოახდინოთ  ვექტორების დამატება და __str__ მეთოდი, რომელიც დააბრუნებს შემდეგი სახის სტრიქონს "(x, y)".
# მაგალითად:
# v1 = Vector(2, 3)
# v2 = Vector(3, 4)
# v3 = v1 + v2
# print(v3)  # Output: (5, 7)

class Vector:
    def __init__(self,x,y):
        self.x = x 
        self.y = y

    def __add__(self, other):

        new_x = self.x + other.x
        new_y = self.y + other.y

        return Vector(new_x,new_y)
    
    def __str__(self):
       
        return f"({self.x}, {self.y})"
    
v1 = Vector(2, 3)
v2 = Vector(3, 4)
v3 = v1 + v2
print(v3)  # Output: (5, 7)

# 2. შექმენით Book კლასი, რომელსაც ექნება ორი ატრიბუტი (სათაური, ავტორი). კლასს შეუქმენით __eq__ მეთოდი რომელიც შეამოწმებს ორი წიგნის ტოლობას.
# ორი წიგნი ითვლება ტოლად თუ მათი სათაურები და ავტორები იდენტურია.

# მაგალითად:
# book1 = Book('1984', 'George Orwell')
# book2 = Book('1984', 'George Orwell')
# book3 = Book('Brave New World', 'Aldous Huxley')
# print(book1 == book2)  # Output: True
# print(book1 == book3)  # Output: False

class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author

    def __eq__(self, other) :
        if isinstance(other, Book):
            return self.author == other.author and self.title == other.title
        

book1 = Book('1984', 'George Orwell')
book2 = Book('1984', 'George Orwell')
book3 = Book('Brave New World', 'Aldous Huxley')
print(book1 == book2)  # Output: True
print(book1 == book3)  # Output: False