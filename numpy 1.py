Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> a = np.array([1, 2, 5, 9], float)
>>> a
array([1., 2., 5., 9.])
>>> a[:2]
array([1., 2.])
>>> a[0:2]
array([1., 2.])
>>> a[-1:2]
array([], dtype=float64)
>>> a = np.array([[1,2,3],[4,5,6]], float)
>>> a[1,:]
array([4., 5., 6.])
>>> a[0,:]
array([1., 2., 3.])
>>> a[:,2]
array([3., 6.])
>>> a.shape
(2, 3)
>>> a(shape)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    a(shape)
NameError: name 'shape' is not defined
>>> a.len
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    a.len
AttributeError: 'numpy.ndarray' object has no attribute 'len'
>>> a.dtype
dtype('float64')
>>> len.a
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    len.a
AttributeError: 'builtin_function_or_method' object has no attribute 'a'
>>> len(a)
2
>>> 2 in a
True
>>> 2 in b
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    2 in b
NameError: name 'b' is not defined
>>> 1 in a
True
>>> 7 in a
False
>>> really
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    really
NameError: name 'really' is not defined
>>> 
