Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> a=np.array([1,2,3])
>>> b=np.array([2,5,4])
>>> np.dot(a,b)
24
>>> np.poly([-1,1,1,10])
array([  1., -11.,   9.,  11., -10.])
>>> #STATISTICS
>>> a=np.array([1,8,6,9])
>>> np.median(a)
7.0
>>> np.mean(a)
6.0
>>> np.random(5)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    np.random(5)
TypeError: 'module' object is not callable
>>> np.random.randn(5)
array([ 0.84119004,  0.06286727,  0.64805966, -0.67940898,  1.20353107])
>>> np.random.rand(5)
array([0.70981707, 0.62592958, 0.42497036, 0.87447216, 0.61663331])
>>> np.random.rand()
0.08207140487396869
>>> np.random.randint()
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    np.random.randint()
  File "mtrand.pyx", line 910, in mtrand.RandomState.randint
TypeError: randint() takes at least 1 positional argument (0 given)
>>> np.random.randint(5)
0
>>> 
>>> np.random.randint(2,70)
43
>>> 
>>> n.random.poisson(9.0)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    n.random.poisson(9.0)
NameError: name 'n' is not defined
>>> np.random.poisson(9.0)
6
>>> np.random.normal(9.0)
8.277177440336686
>>> 
