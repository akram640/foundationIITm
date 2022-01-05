## Definations

#### Objects -> *Objects are entities that have certain attributes along with operations associated with them.* 


#### Class -> *A class is a blueprint or a template that is used to create objects.*


#### *Object Oriented Programming (OOP) is a paradigm that looks at the world as a collection of objects and the interactions among them.* 


## Classes and Objects

1. Attributes define the state of an object. Different objects of the same class could have different attributes.

2. Naively speaking, methods help to update the values of the attributes.
   Therefore, the methods capture the behaviour of the object.

## Self

1. The variable self is used to point to the current object.




## Class Attributes vs Object Attributes


```
class Student:
    counter = 0
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        Student.counter += 1
           
    def update_marks(self, marks):
        self.marks = marks
        
    def print_details(self):
        print(f'{self.name}:{self.marks}')
  ```


1. An attribute that is common to all objects and is not tied to any individual object. 

2. If the same attribute name occurs in both an object and a class, then Python prioritizes the object attribute.


3. object attributes can be created dynamically during runtime. 

```
   class Student:
       def __init__(self, name):
           self.name = name

   anish = Student('Anish')
   anish.maths = 100
   anish.physics = 90
   anish.chem = 70

```
