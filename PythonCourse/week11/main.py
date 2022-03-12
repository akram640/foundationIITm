a = [4,1,0,2,3]
b = [5,2,9,2,9]

def sub(x,y):
    return x - y

c = map(sub, a, b)
print(list(c))
