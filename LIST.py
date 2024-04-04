'''
names=['swathi','indhu','abi',]
names2=['dhivi','sindhu']
print(names)
print(type(names))

names.append('avina')
print(names)

names.extend(names2)
print(names)

names.insert(1,'chithu')
print(names)

names.remove('swathi')
print(names)

names.pop()
print(names)

print(names.index("abi",1))

print(names.count('chithu'))

names.sort()
print(names)

names.reverse()
print('reverse list:',names)

names3=names.copy()
print('copied list',names3)

names3.clear()
print(names)
'''

#example
a=[]
print(any(a))
for x in range(10):
    a.append(x*2)
print(a)

a=[x**2 for x in range(7)]
print(a)

print(sum(a))

print(min(a))


print(any(a))


a=[x**2 for x in range(10) if x%3==0]
print(a)


a=[x+y for x in ["new","element","one"] for y in ["a","b","c"] ]
print(a)

