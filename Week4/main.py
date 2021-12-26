l = [5,4,3,2,1,0]

x = []

for i in range(len(l)-1):
    least = min(l)
    x.append(least)
    l.remove(least)

print(x)
