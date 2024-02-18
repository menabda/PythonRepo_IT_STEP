# 1. შექმენით პითონის კლასი Node რომელსაც ექნება ორი ატრიბუტი (value, next), შემდეგ შექმენით LinkedList  კლასი რომლის კონსტრუქტორი მიიღებს Value პარამეტრს.
# 2. LinkedList კლასში შექმენით append მეთოდი, რომლის საშუალებითაც ჩაამტებთ სიის ბოლოში ახალ ნოუდს (Node  კლასის ახალ ობიექტს)
# 3. LinkedList კლასში შექმენით remove მეთოდი, რომლის საშუალებითაც წაშლით სიიდან მის ბოლო ელემენტს(Тail-ს)
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        new_node = Node(value)
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def remove(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    def display(self):
        current = self.head
        print("<------>")
        while current:
            print(current.value)
            current = current.next
        print("<------>")

if __name__ == "__main__":
    linked_list = LinkedList(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.display()  
    linked_list.remove()
    linked_list.display()  
# 4. პითონის Stack.py ფაილში შექმენილია Stack კლასი, დაწერეთ კლასის ფუნქციები (push და pop)
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        return self.stack.pop()
        

st = Stack()
st.push(1)
st.push(2)
st.push(1)
st.push(2)
st.pop()
print(st.stack)
