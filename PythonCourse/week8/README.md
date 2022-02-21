*Programming requires practice*

## L8.1: Introudction to recursion
1) Recursion
2) More Programming
3) File handling


What is recursion ?

`Washing 10 vassel = Washing 1 vassel + Outsourcing`

`L(n) = L(1) + L(n-1)` L -> Living

`T(n) = 1 + T(n-1)` Covid spread i.e. Covid is recursive

***

## L8.2: Recursion: a simple question

<img width="403" alt="image" src="https://user-images.githubusercontent.com/52348635/154889296-fbf7e1ff-2ded-47fa-a925-3b7b834973bf.png">

***

## L8.3: Recursion: find 0 in a list

```python

'''This is a piece of code to check if a given list has 0 in it or not.
If it has "zero" in it we return True'''

def check0(L):
  #if the list is empty, return False
  if (len(L)==0):
      return 0
  if (L[0]==0):
      return 1
  else:
      return check0(L[1:len(L)])
```

***

## L8.4: Sorting Recursively

```python

def Sort(L):
  '''recursively sort the list L'''
  if (L==[]):
      return L
   m = min(L)
   L.remove(m)
   return [m] + Sort(L)

```

***

## L8.5: Introduction to Binary Search

<img width="576" alt="image" src="https://user-images.githubusercontent.com/52348635/154893869-806e4594-cb0f-4fa1-82b3-a6d279447d80.png">

*** 

## L8.6: Warm up for Binary Search

```python
def obvious_search(L,k):
    for x in L:
        if x == k:
            return True
    return False
```
`import filename`.  This is how to use function from another file

***

## L8.7: 

