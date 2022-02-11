*IF you want to gain something in life then you have to give something in life*

## L6.1:  Lists and Sets

```python
y = {1,2,1,2,34} # this is a set in Python
```

* Set is faster when searching an element in set
* Searching in list is very defficult
* Set takes roughly 10 times more space than a **list sizeof(set) > sizeof(list)**
* Element in set are not inorder.
* Set is best for searching operation

***

## L6.2: Dictionaries

```python
d = {} # this is a dictionary
d['akram'] = 98.98
d['rahul'] = 88.99

print(d) # {'akram':98.98,'rahul':88.99}
```
dictionary is ``{key:value}`` pairs

***

## L6.3: Tuples

```python
t = (1,2,3,4,5)
# A tuples is unchangle immutable
# List is flexible and tuple is not flexible
```
* Tuple takes less space than list

***


## L6.4: More on Lists

```python
l1 = [1,2,3]
l2 = [10,20,30]
l12 = l1 + l2 # This will add two list

l = [0]*10 # l = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

l1 = [1,2,3]
l2 = [1,2,3]
print(l1==l2)
```

* Lists are compared one element at a t time

```python
l1 = [1,2,3]
l2 = l1
print(l1 is l2) # True
l3 = list(l1)
print(l1 is l3) # False

```








