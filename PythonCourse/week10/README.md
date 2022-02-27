# Week 10

## L10.1: Introduction to Object Orented Programming (OOP)





***

## L10.2: Classes and Objects

* Classes is like blueprint
* Real object are made from blueprint

```python
# BluePrint for Student
class Student:
    roll_no = None
    name = None

# Created a real student s0
s0 = Student() # This is inbuilt constructor
s0.roll_no = 0
s0.name = "Bhuvanesh"

print(s0.roll_no,s0.name)

s1 = Student()
print(s1.roll_no,s1.name)

s2 = Student()
s2.roll_no = 2
s2.name = "Harish"
print(s2.roll_no,s2.name)


```

***

## L10.3: Attributes and Methods

```python
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

# __init__(), display(), result() are method

s0 = Student(0,'Bhuvanesh',100) # constructor
s0.display()
s0.result()
s1 = Student(1,'Harish',150) #constructor
s1.display()
s1.result()
```
***
