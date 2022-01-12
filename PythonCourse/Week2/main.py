s = input()
a = int(input())
b = int(input())

subs = s[a:b+1]

mul = len(s)//len(subs)

subs = subs*(mul+1)

print(subs)


for i in range(199):
    print(i)
