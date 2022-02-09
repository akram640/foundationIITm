def some_funtion(word):
    space = ' '
    if space in word:
        return False

    if not('A' <= word[0] <= 'Z'):
        return False
    for i in range(1,len(word)):
        if not('a' <= word[i] <= 'z'):
            return False

    return True

print(some_funtion('Riemann'))
