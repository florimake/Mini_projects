
x = "cesafdasY"
i = []
for a in range(0, len(x), 2):
    if a < len(x)-1:
        i.append(x[a:a+2]) 
    else:
        i.append(x[a]+ "_") 
print(i)

  
p=[x[a]+x[a+1] if a < len(x)-1 else x[a]+ "_" for a in range(0, len(x), 2) ]
s = [(x + "_")[i:i + 2] for i in range(0, len(x), 2)]

print(s)
print(p)

m1 = [1,2,3,4,5]
m2 = [10,20,30,40]
m3 = [100,200,300,400]

print(list(zip(m1,m2,m3)))
print(list(iter(x)))

y=''
for i in range(len(x)):
    if x[i] == 'a':
        y += x[i]+'*'
    else:
        y += x[i]

z= ''.join([x[i]+'*' if x[i] == 'a' else x[i] for i in range(len(x))])
print(y)
print(x)
print(z)

print(2+-2/2+2)
print(m1[2] in m1)
nm = m1[:4]
print(m1[:4].pop())
print(min(m1))
