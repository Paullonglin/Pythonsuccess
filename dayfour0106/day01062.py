dict={'a':1,'b':2}
dict['a']=3
dict['c']=5
del dict['b']
print(dict.keys())
print(dict.values())
print(len(dict))
list=list(dict.values())
print(type(dict.values()))
print(type(list))