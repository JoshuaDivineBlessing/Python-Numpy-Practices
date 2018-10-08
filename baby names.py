Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a='monkey'
>>> a[0::2]
'mne'
>>> a='monkeya'
>>> a[0::2]
'mnea'
>>> import pandas as pd
names
>>> import pandas as pd
>>> names1880 = pd.read_csv('names/yob1880.txt', names=['name', 'sex', 'births')
			    
SyntaxError: invalid syntax
>>> names1880 = pd.read_csv('names/yob1880.txt', names=['name', 'sex', 'births'])
			    
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    names1880 = pd.read_csv('names/yob1880.txt', names=['name', 'sex', 'births'])
  File "C:\Users\Joshua\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pandas\io\parsers.py", line 678, in parser_f
    return _read(filepath_or_buffer, kwds)
  File "C:\Users\Joshua\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pandas\io\parsers.py", line 440, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "C:\Users\Joshua\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pandas\io\parsers.py", line 787, in __init__
    self._make_engine(self.engine)
  File "C:\Users\Joshua\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pandas\io\parsers.py", line 1014, in _make_engine
    self._engine = CParserWrapper(self.f, **self.options)
  File "C:\Users\Joshua\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pandas\io\parsers.py", line 1708, in __init__
    self._reader = parsers.TextReader(src, **kwds)
  File "pandas\_libs\parsers.pyx", line 384, in pandas._libs.parsers.TextReader.__cinit__
  File "pandas\_libs\parsers.pyx", line 695, in pandas._libs.parsers.TextReader._setup_parser_source
FileNotFoundError: File b'names/yob1880.txt' does not exist
>>> names1880 = pd.read_csv('names/yob1880.txt', names=['name', 'sex', 'births'])
			    
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    names1880 = pd.read_csv('names/yob1880.txt', names=['name', 'sex', 'births'])
  File "C:\Users\Joshua\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pandas\io\parsers.py", line 678, in parser_f
    return _read(filepath_or_buffer, kwds)
  File "C:\Users\Joshua\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pandas\io\parsers.py", line 440, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "C:\Users\Joshua\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pandas\io\parsers.py", line 787, in __init__
    self._make_engine(self.engine)
  File "C:\Users\Joshua\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pandas\io\parsers.py", line 1014, in _make_engine
    self._engine = CParserWrapper(self.f, **self.options)
  File "C:\Users\Joshua\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pandas\io\parsers.py", line 1708, in __init__
    self._reader = parsers.TextReader(src, **kwds)
  File "pandas\_libs\parsers.pyx", line 384, in pandas._libs.parsers.TextReader.__cinit__
  File "pandas\_libs\parsers.pyx", line 695, in pandas._libs.parsers.TextReader._setup_parser_source
FileNotFoundError: File b'names/yob1880.txt' does not exist
>>> names1880 = pd.read_csv('E:\yob1880.txt', names=['name', 'sex', 'births'])
			    
>>> names1800
			    
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    names1800
NameError: name 'names1800' is not defined
>>> names1880
			    
           name sex  births
0          Mary   F    7065
1          Anna   F    2604
2          Emma   F    2003
3     Elizabeth   F    1939
4        Minnie   F    1746
5      Margaret   F    1578
6           Ida   F    1472
7         Alice   F    1414
8        Bertha   F    1320
9         Sarah   F    1288
10        Annie   F    1258
11        Clara   F    1226
12         Ella   F    1156
13     Florence   F    1063
14         Cora   F    1045
15       Martha   F    1040
16        Laura   F    1012
17       Nellie   F     995
18        Grace   F     982
19       Carrie   F     949
20        Maude   F     858
21        Mabel   F     808
22       Bessie   F     796
23       Jennie   F     793
24     Gertrude   F     787
25        Julia   F     783
26       Hattie   F     769
27        Edith   F     768
28       Mattie   F     704
29         Rose   F     700
...         ...  ..     ...
1970      Philo   M       5
1971    Phineas   M       5
1972    Presley   M       5
1973     Ransom   M       5
1974      Reece   M       5
1975       Rene   M       5
1976    Roswell   M       5
1977    Rowland   M       5
1978    Sampson   M       5
1979     Samual   M       5
1980     Santos   M       5
1981   Schuyler   M       5
1982   Sheppard   M       5
1983   Spurgeon   M       5
1984   Starling   M       5
1985   Sylvanus   M       5
1986   Theadore   M       5
1987  Theophile   M       5
1988     Tilmon   M       5
1989      Tommy   M       5
1990    Unknown   M       5
1991       Vann   M       5
1992        Wes   M       5
1993    Winston   M       5
1994       Wood   M       5
1995     Woodie   M       5
1996     Worthy   M       5
1997     Wright   M       5
1998       York   M       5
1999  Zachariah   M       5

[2000 rows x 3 columns]
>>> 
