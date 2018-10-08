Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #data structures
>>> """List
Tuple
Dictionary
Set"""
'List\nTuple\nDictionary\nSet'
>>> a = []
>>> type(a)
<class 'list'>
>>> len(a)
0
>>> a.append(1)
>>> a
[1]
>>> a.append(5.5)
>>> a
[1, 5.5]
>>> a.append('hello')
>>> a
[1, 5.5, 'hello']
>>> my_list = [100,250,88.90,'python']
>>> my_list
[100, 250, 88.9, 'python']
>>> a[0]
1
>>> a
[1, 5.5, 'hello']
>>> my_list[0]
100
>>> my_list[-1]
'python'
>>> my_list[0:2]
[100, 250]
>>> a.append('hello','thor')
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    a.append('hello','thor')
TypeError: append() takes exactly one argument (2 given)
>>> a.append(['hello','thor'])
>>> a
[1, 5.5, 'hello', ['hello', 'thor']]
>>> a[-1]
['hello', 'thor']
>>> a[-1][-1]
'thor'
>>> a[-1][-1][-1]
'r'
>>> a
[1, 5.5, 'hello', ['hello', 'thor']]
>>> a.pop()
['hello', 'thor']
>>> a
[1, 5.5, 'hello']
>>> my_list.pop(2)
88.9
>>> aq
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    aq
NameError: name 'aq' is not defined
>>> a
[1, 5.5, 'hello']
>>> my_list
[100, 250, 'python']
>>> a + my_list
[1, 5.5, 'hello', 100, 250, 'python']
>>> dir(list)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> dir(my_list)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> a
[1, 5.5, 'hello']
>>> a.remove(5.5)
>>> a
[1, 'hello']
>>> a.insert(1,5.5)
>>> a
[1, 5.5, 'hello']
>>> a.insert(3,5.5)
>>> a
[1, 5.5, 'hello', 5.5]
>>> a.insert(3,890)
>>> a
[1, 5.5, 'hello', 890, 5.5]
>>> a.remove(5.5)
>>> a
[1, 'hello', 890, 5.5]
>>> a.insert(1,5.5)
>>> a
[1, 5.5, 'hello', 890, 5.5]
>>> a.count(5.5)
2
>>> a.index(5.5)
1
>>> a
[1, 5.5, 'hello', 890, 5.5]
>>> a.index(5.5,[2,4])
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    a.index(5.5,[2,4])
TypeError: slice indices must be integers or have an __index__ method
>>> b = a.copy()
>>> b
[1, 5.5, 'hello', 890, 5.5]
>>> c = a
>>> c
[1, 5.5, 'hello', 890, 5.5]
>>> id(a)
56043480
>>> id(c)
56043480
>>> id(b)
55936224
>>> a
[1, 5.5, 'hello', 890, 5.5]
>>> a.reverse()
>>> a
[5.5, 890, 'hello', 5.5, 1]
>>> dir(a)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> a + my_list
[5.5, 890, 'hello', 5.5, 1, 100, 250, 'python']
>>> a
[5.5, 890, 'hello', 5.5, 1]
>>> a.extend(my_list)
>>> A
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    A
NameError: name 'A' is not defined
>>> a
[5.5, 890, 'hello', 5.5, 1, 100, 250, 'python']
>>> a.extend([56,78,9.8])
>>> a
[5.5, 890, 'hello', 5.5, 1, 100, 250, 'python', 56, 78, 9.8]
>>> #Tuple
>>> e = (1,2.5,'python',767889)
>>> type(e)
<class 'tuple'>
>>> a
[5.5, 890, 'hello', 5.5, 1, 100, 250, 'python', 56, 78, 9.8]
>>> a[0] =100
>>> a
[100, 890, 'hello', 5.5, 1, 100, 250, 'python', 56, 78, 9.8]
>>> e[0] = 100
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    e[0] = 100
TypeError: 'tuple' object does not support item assignment
>>> e
(1, 2.5, 'python', 767889)
>>> dir(e)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
>>> e[0]
1
>>> #Dictionary
>>> k = {}
>>> type(k)
<class 'dict'>
>>> k['name'] = 'Tom'
>>> k
{'name': 'Tom'}
>>> k['age'] = 25
>>> k
{'name': 'Tom', 'age': 25}
>>> k['gender'] = 'M'
>>> k
{'name': 'Tom', 'age': 25, 'gender': 'M'}
>>> k['class'] = 'First class'
>>> k
{'name': 'Tom', 'age': 25, 'gender': 'M', 'class': 'First class'}
>>> k['Marks'] = [34,67,89]
>>> k
{'name': 'Tom', 'age': 25, 'gender': 'M', 'class': 'First class', 'Marks': [34, 67, 89]}
>>> k['Marks']
[34, 67, 89]
>>> k['Marks'][0]
34
>>> dir(dict)
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
>>> k.pop('gender')
'M'
>>> k
{'name': 'Tom', 'age': 25, 'class': 'First class', 'Marks': [34, 67, 89]}
>>> k.values()
dict_values(['Tom', 25, 'First class', [34, 67, 89]])
>>> k.keys()
dict_keys(['name', 'age', 'class', 'Marks'])
>>> k.items()
dict_items([('name', 'Tom'), ('age', 25), ('class', 'First class'), ('Marks', [34, 67, 89])])
>>> k.get('name')
'Tom'
>>> k.fromkeys('name')
{'n': None, 'a': None, 'm': None, 'e': None}
>>> k.fromkeys(['name'])
{'name': None}
>>> help(dict.fromkeys)
Help on built-in function fromkeys:

fromkeys(iterable, value=None, /) method of builtins.type instance
    Returns a new dict with keys from iterable and values equal to value.

>>> k
{'name': 'Tom', 'age': 25, 'class': 'First class', 'Marks': [34, 67, 89]}
>>> k['name']='sam'
>>> k
{'name': 'sam', 'age': 25, 'class': 'First class', 'Marks': [34, 67, 89]}
>>> a
[100, 890, 'hello', 5.5, 1, 100, 250, 'python', 56, 78, 9.8]
>>> 'python' in a
True
>>> 78 in a
True
>>> 1000 in a
False
>>> b
[1, 5.5, 'hello', 890, 5.5]
>>> c
[100, 890, 'hello', 5.5, 1, 100, 250, 'python', 56, 78, 9.8]
>>> a
[100, 890, 'hello', 5.5, 1, 100, 250, 'python', 56, 78, 9.8]
>>> b = a.copy()
>>> b
[100, 890, 'hello', 5.5, 1, 100, 250, 'python', 56, 78, 9.8]
>>> a
[100, 890, 'hello', 5.5, 1, 100, 250, 'python', 56, 78, 9.8]
>>> c
[100, 890, 'hello', 5.5, 1, 100, 250, 'python', 56, 78, 9.8]
>>> a == c
True
>>> a is c
True
>>> a == b
True
>>> a is b
False
>>> #control flow
>>> for i in [1,2,3,4]:
	print(i**2)
	print(i**3)

	
1
1
4
8
9
27
16
64
>>> for j in a:
	print(j)

	
100
890
hello
5.5
1
100
250
python
56
78
9.8
>>> for j in a:
	print(j,end =' ')

	
100 890 hello 5.5 1 100 250 python 56 78 9.8 
>>> for j in a:
	print(j,end =',')

	
100,890,hello,5.5,1,100,250,python,56,78,9.8,
>>> for i in 'python':
	print(i)

	
p
y
t
h
o
n
>>> for i in 'perl':
	for j in 'gan':
		print(i+j)

		
pg
pa
pn
eg
ea
en
rg
ra
rn
lg
la
ln
>>> m = 10
>>> n = 5
>>> if m > n:
	print('m is big')
elif m == n:
	print('both are sdam')
else:
	print('m is smal')

	
m is big
>>> if m > n:print('m is big')

m is big
>>> while m > n:
	print('m is big')
	break

m is big
>>> while m > n:
	print('m is big')
	n += 1

	
m is big
m is big
m is big
m is big
m is big
>>> list('python')
['p', 'y', 't', 'h', 'o', 'n']
>>> ''.join(list('python'))
'python'
>>> ' '.join(list('python'))
'p y t h o n'
>>> def my_func1():
	return 2**3

>>> my_func1()
8
>>> def my_func2():
	print(2**3)

	
>>> my_func2()
8
>>> a = my_func1()
>>> b = my_func2()
8
>>> a
8
>>> b
>>> def my_func3(x):
	return x+5

>>> my_func3(4)
9
>>> def my_func4(x,y):
	return x+y+5

>>> my_func4(3)
Traceback (most recent call last):
  File "<pyshell#183>", line 1, in <module>
    my_func4(3)
TypeError: my_func4() missing 1 required positional argument: 'y'
>>> my_func4(3,7)
15
>>> def my_func4(x,y=6):
	return x+y+5

>>> my_func4(3)
14
>>> my_func4(3,7)
15
>>> def my_func4(y=6,x=2):
	return x+y+5

>>> my_func4()
13
>>> my_func4(x = 8)
19
>>> my_func4(x = 8,y=13)
26
>>> my_func4(y=13,x=8)
26
>>> def my_func5(y=6,x):
	return x+y+5
SyntaxError: non-default argument follows default argument
>>> def my_func4(*v):
	return sum(v)

>>> my_func4(4,56,789990,7.5,7988)
798045.5
>>> def my_func5(x,*v):
	return sum(v),x

>>> my_func4(4,56,789990,7.5,7988)
798045.5
>>> def my_func5(x,*v):
	print(x)
	return sum(v)

>>> my_func4(4,56,789990,7.5,7988)
798045.5
>>> my_func5(4,56,789990,7.5,7988)
4
798041.5
>>> def my_func5(*v,x):
	print(x)
	return sum(v)

>>> my_func5(4,56,789990,7.5,7988)
Traceback (most recent call last):
  File "<pyshell#208>", line 1, in <module>
    my_func5(4,56,789990,7.5,7988)
TypeError: my_func5() missing 1 required keyword-only argument: 'x'
>>> my_func5(4,56,789990,7.5,7988,x=25)
25
798045.5
>>> def my_func7(**kw):
	print(type(kw))
	return sum(kw)

>>> my_func7(a=10,x=45,y=456,i=466,j=7697)
<class 'dict'>
Traceback (most recent call last):
  File "<pyshell#212>", line 1, in <module>
    my_func7(a=10,x=45,y=456,i=466,j=7697)
  File "<pyshell#211>", line 3, in my_func7
    return sum(kw)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> def my_func7(**kw):
	print(type(kw))
	print(kw)
	return sum(kw)

>>> my_func7(a=10,x=45,y=456,i=466,j=7697)
<class 'dict'>
{'a': 10, 'x': 45, 'y': 456, 'i': 466, 'j': 7697}
Traceback (most recent call last):
  File "<pyshell#215>", line 1, in <module>
    my_func7(a=10,x=45,y=456,i=466,j=7697)
  File "<pyshell#214>", line 4, in my_func7
    return sum(kw)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> dir(dict)
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
>>> def my_func7(**kw):
	print(type(kw))
	print(kw)
	return sum(kw.values())

>>> my_func7(a=10,x=45,y=456,i=466,j=7697)
<class 'dict'>
{'a': 10, 'x': 45, 'y': 456, 'i': 466, 'j': 7697}
8674
>>> 
