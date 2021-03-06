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

Iterator

```python
fruits = ['mango','apple','banana','orange','guava']

for fruit in fruits:
    print(fruit)
```
Iterator

```python
fruits = ['mango','apple','banana','orange','guava']


bascket = iter(fruits)

print(bascket)

print(next(bascket))
print(next(bascket))
print(next(bascket))
print(next(bascket))

```
```python

def square(limit):
    x = 0
    while x < limit:
        yield x * x
        yield x * x * x
        x += 1

a = square(5)
print(next(a),next(a))
print(next(a),next(a))
print(next(a),next(a))
print(next(a),next(a))
print(next(a),next(a))

```
***

## L11.4: Functional Programming (Part 2)

```python
a = 10
b = 20
if a < b:
    small = a
else:
    small = b

print(small)
```
Python way

```python
a = 10
b = 20
small = a if a < b else b
```

List comprehension
```python
fruits = ['mango','apple','banana','orange','guava']

'''newList = []
for fruit in fruits:
    if 'n' in fruit:
        newList.append(fruit.capitalize())
'''
newList = [fruit.capitalize() for fruit in fruits if 'n' in fruit]
print(newList)
```
***

## L11.5: Functional Programming (Part 3)

Lambda function

```python
add = lambda x,y: x + y
sub = lambda x,y: x - y
mul = lambda x,y: x * y
div = lambda x,y: x / y

print(add(10,20))
print(sub(10,20))
print(mul(10,20))
print(div(10,20))
```
zip 

```python
fruits = ['mango','apple','banana','orange','guava']

size = [4,1,0,2,3]

print(dict(zip(fruits,size))) # {'mango': 4, 'apple': 1, 'banana': 0, 'orange': 2, 'guava': 3}
```
map

```python
a = [4,1,0,2,3]
b = [5,2,9,2,9]

def sub(x,y):
    return x - y

c = map(sub, a, b)
print(list(c)) # output -> [-1, -1, -9, 0, -6]
```
