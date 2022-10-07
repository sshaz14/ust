myset = {1,1,1,2,2,2,2,3,4,5,6,6,6,6,7,8}
print(myset)
print(len(myset))

myset1 = {1.11,2.22,2.34,5.66,6.67,8.00}
print(myset1)


myset2={'Mickey', 'Jerry',"Donald"}
print(myset2)

myset3={12, 13, 'Mickey', 'Jerry','Donald'}
print(myset3)

myset4 = set()
print(type(myset4))

myset5 = set(('one','two','three','four'))

for i in myset5:
    print(i)

for i in enumerate (myset5):
    print(i)

print('two' in myset5)
print('eight' in myset5)

if 'eight' in myset5:
    print('value eight is present in myset5')
else:
    print('value eight is not present in myset5')

#add & remove items in sets
myset = set(('one','two','three','four'))
myset.add('five')
myset.update(['six', 'seven'])
print(myset)
myset.remove('six')
print(myset)
myset.discard('five')
print(myset)
myset.clear()
print(myset)
myset = set(('one','two','three','four'))
myset1=myset
myset2=myset.copy()
print(id(myset), id(myset1), id(myset2))
myset.add('nine')

print(myset1, myset2)

