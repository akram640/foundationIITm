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
