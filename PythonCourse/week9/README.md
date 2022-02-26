*Life is full of trade-off*
# Week 9
* File Handling
* Pandas - Data Sciences

## L9.1: Introudction to File Handling

<img width="518" alt="image" src="https://user-images.githubusercontent.com/52348635/155841471-ff3cd20c-2464-44e6-ae53-9e8005feeee2.png">

On your computer you have two types of storage

<img width="482" alt="image" src="https://user-images.githubusercontent.com/52348635/155841525-a1cb5f19-13de-45a8-b1b1-95b168c46a90.png">

How to handle files using Python ?

***

## L9.2: Reading and Writing to a File

```python
f=open('mytext.txt','w') # this will create a file mytext.txt in writing mode
f.write('akram ') # This will write 'akram' to f
f.write('IIT ')
f.write('India ')
f.write('Python ')
f.close() # This close the f

# Now opening the file in reading mode
x=open('mytext.txt','r')
s = x.read()
x.close()

```

***

## L9.3: Big text file handling

<img width="714" alt="image" src="https://user-images.githubusercontent.com/52348635/155842598-5b7afc0e-c4fd-4683-b7f6-907c9bf1cf64.png">

***

## L9.4: Very big files - a tip
A big file may not open (12GB of size)
you can go line by line
it will never get hang

<img width="676" alt="image" src="https://user-images.githubusercontent.com/52348635/155842828-de0b265a-89b2-42ba-a8b2-29c463fc0b26.png">

File handling is possible no matter how big the file is


