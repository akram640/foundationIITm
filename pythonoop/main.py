class Student:
    counter = 0 # this a is class attribute
    def __init__(self,name,marks):
        self.name = name # name is attribute of the object
        self.marks = marks # marks is attribute of the object
        Student.counter += 1

    def update_marks(self,marks):
        self.marks = marks

    def print_details(self):
        print(f'{self.name}:{self.marks}')

madhavan = Student('Madhavan',90)
print(f'Number of student in the program = {Student.counter}')
Andrew = Student('Adrew',80)
print(f'Number of student in the program = {Student.counter}')

print(madhavan.counter)
madhavan.counter = -1
print(Student.counter)
print(madhavan.counter)
