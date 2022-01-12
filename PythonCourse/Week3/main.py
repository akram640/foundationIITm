word = input()
valid = False

if 'a' <= word[0] <= 'z':
    if word[0] == word[-1]:
        valid = True
print(valid)
