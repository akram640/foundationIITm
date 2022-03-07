# Week 11

## L11.1: Introduction

1. Exceptional handling
2. Functional programming

***

## L11.2: Exception handling

```python
a = int(input())
b = int(input())

c = a / b # It will fail when b as input is 0
print(c)

```
Now This code will not fail when b is 0 as input

```python
a = int(input())
b = int(input())

try:
    c = a/b
    print(c)
except ZeroDivisionError:
    print('Invalid input, divisor can not be zero')
```
This will handle all error at the same time (ZeroDivisionError,Variable not defined,FileNotFoundError)

```python
a = int(input())
b = int(input())

try:
    c = a/b
    print(c)
    f = open('abc.txt','r')
except ZeroDivisionError:
    print('Invalid input, divisor can not be zero')

except NameError:
    print('Variable not defined')
except FileNotFoundError:
    print('Invalid file name. Please check again')
```

This will handle all types of errors (In Python there is 37 Exception)

```python
a = int(input())
b = int(input())

try:
    c = a/b
    print(c)
    f = open('abc.txt','r')
except ZeroDivisionError:
    print('Invalid input, divisor can not be zero')

except NameError:
    print('Variable not defined')
except FileNotFoundError:
    print('Invalid file name. Please check again')
except:
    print('Something went wrong')
```

Some exception python also does not know

* User defined exception

```python
a = int(input())
if a < 18:
    raise Exception('You are underage, you can not vote')
```

***

## L11.3: Functional Programming (Part 1)

 

