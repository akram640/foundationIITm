class Student:
    count = 0
    def __init__(self,roll_no,name,total):
        self.roll_no = roll_no
        self.name = name
        self.total = total
        Student.count += 1

    def display(self):
        print(self.roll_no,self.name,self.total)

    def result(self):
        if self.total > 120:
            print("Pass")
        else:
            print("Fail")

s0 = Student(0,'Bhuvanesh',100) # constructor
s0.display()
s0.result()
s1 = Student(1,'Harish',150) #constructor
s1.display()
s1.result()

