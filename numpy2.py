Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> a = np.array(range(15))
>>> a
array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14])
>>> a.reshape(6,3)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    a.reshape(6,3)
ValueError: cannot reshape array of size 15 into shape (6,3)
>>> a.reshape(5,3)
array([[ 0,  1,  2],
       [ 3,  4,  5],
       [ 6,  7,  8],
       [ 9, 10, 11],
       [12, 13, 14]])
>>> b=a
>>> c=a.copy()
>>> c=
SyntaxError: invalid syntax
>>> c
array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14])
>>> 

>>> a.tolist()
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
>>> a.tostring()
b'\x00\x00\x00\x00\x01\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00\x04\x00\x00\x00\x05\x00\x00\x00\x06\x00\x00\x00\x07\x00\x00\x00\x08\x00\x00\x00\t\x00\x00\x00\n\x00\x00\x00\x0b\x00\x00\x00\x0c\x00\x00\x00\r\x00\x00\x00\x0e\x00\x00\x00'
>>> #FILL ARRAY WITH A SINGLE VALUE
>>> a.fill(23)
>>> a
array([23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23])
>>> a
array([23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23])
>>> a = np.array(range(10)).reshape((2,3))
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    a = np.array(range(10)).reshape((2,3))
ValueError: cannot reshape array of size 10 into shape (2,3)
>>> a = np.array(range(10))
>>> a
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> a.reshape(5,2)
array([[0, 1],
       [2, 3],
       [4, 5],
       [6, 7],
       [8, 9]])
>>> a.T
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> a.transpose()
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> a.reshape(5,2)
array([[0, 1],
       [2, 3],
       [4, 5],
       [6, 7],
       [8, 9]])
>>> a.transpose()
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> a
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> a=a.reshape(5,2)
>>> a
array([[0, 1],
       [2, 3],
       [4, 5],
       [6, 7],
       [8, 9]])
>>> a=a.transpose()
>>> a
array([[0, 2, 4, 6, 8],
       [1, 3, 5, 7, 9]])
>>> a.flatten()
array([0, 2, 4, 6, 8, 1, 3, 5, 7, 9])
>>> b=np.array([5,6,8])
>>> np.concatenate(a,b)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    np.concatenate(a,b)
TypeError: only integer scalar arrays can be converted to a scalar index
>>> np.concatenate((a,b))
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    np.concatenate((a,b))
ValueError: all the input arrays must have same number of dimensions
>>> a=np.array([2,9])
>>> b=np.array([3,2,5])
>>> np.concatenate((a,b,c))
array([ 2,  9,  3,  2,  5,  0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11,
       12, 13, 14])
>>> a[:,np.newaxis]
array([[2],
       [9]])
>>> np.arange(5)
array([0, 1, 2, 3, 4])
>>> np.ones((3,5))
array([[1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 1.]])
>>> np.twos((3,4))
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    np.twos((3,4))
AttributeError: module 'numpy' has no attribute 'twos'
>>> np.identify(4)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    np.identify(4)
AttributeError: module 'numpy' has no attribute 'identify'
>>> np.identity(4)
array([[1., 0., 0., 0.],
       [0., 1., 0., 0.],
       [0., 0., 1., 0.],
       [0., 0., 0., 1.]])
>>> np.sqrt(a)
array([1.41421356, 3.        ])
>>> np.pi
3.141592653589793
>>> a=np.array([1.3, 1.5, 1.1, 0.2])
>>> np.rint(a)
array([1., 2., 1., 0.])
>>> a=np.array(range(10))
>>> for x in a:
	print x
	
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(x)?
>>> for x in a:
	print(x)
	return
SyntaxError: 'return' outside function
>>> print x
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(x)?
>>> print(x)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    print(x)
NameError: name 'x' is not defined
>>> for x in a:
	print(x)
	<hit return>
	
SyntaxError: invalid syntax
>>> for x in a:
	print(x)

	
0
1
2
3
4
5
6
7
8
9
>>> a=np.array([2,4,3])
>>> a.sum()
9
>>> a.prod()
24
>>> a.mean()
3.0
>>> a.var()
0.6666666666666666
>>> a.std()
0.816496580927726
>>> a.min()
2
>>> a.max()
4
>>> 
a.sort()
>>> 
>>> a
array([2, 3, 4])
>>> a=np.array([5,2,0.01, 56,25,-5])
>>> a.sort()
>>> a
array([-5.0e+00,  1.0e-02,  2.0e+00,  5.0e+00,  2.5e+01,  5.6e+01])
>>> a.sort(float)
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    a.sort(float)
TypeError: an integer is required (got type type)
>>> a
array([-5.0e+00,  1.0e-02,  2.0e+00,  5.0e+00,  2.5e+01,  5.6e+01])
>>> a=np.array([5,1,6,0.1])
>>> a>2
array([ True, False,  True, False])
>>> 
