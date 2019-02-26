a=['a','b']
b=['1','2']
print(dict(zip(a,b)))
c=tuple(b)
print(c)
dict=dict.fromkeys(c)
print(dict.get('1'))

