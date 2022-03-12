fruits = ['mango','apple','banana','orange','guava']

newList = []
for fruit in fruits:
    if 'n' in fruit:
        newList.append(fruit.capitalize())
print(newList)
