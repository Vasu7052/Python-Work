Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 3/3
1.0
>>> 5/2.5
2.0
>>> 7/3
2.3333333333333335
>>> 3*5
15
>>> clr
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    clr
NameError: name 'clr' is not defined
>>> clear
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    clear
NameError: name 'clear' is not defined
>>> clrscr
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    clrscr
NameError: name 'clrscr' is not defined
>>> 8+2*10
28
>>> 18/4
4.5
>>> 18//4
4
>>> 7//3
2
>>> 2%1
0
>>> 5%2
1
>>> 5**3
125
>>> num = 5.0
>>> str = "Hey"
>>> str = HEY
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    str = HEY
NameError: name 'HEY' is not defined
>>> num2 = 2
>>> num2/num
0.4
>>> str = 'HEY'
>>> str
'HEY'
>>> num2
2
>>> "HEYA"
'HEYA'
>>> print("jsdbvkjdbsv")
jsdbvkjdbsv
>>> print('c:\k\bdbf')
c:\kdbf
>>> print(r"\n")
\n
>>> str = "Vasu"
>>> str2 = "Gupta"
>>> print(str+str2)
VasuGupta
>>> str+str2
'VasuGupta'
>>> str+=str2
>>> str
'VasuGupta'
>>> str*5
'VasuGuptaVasuGuptaVasuGuptaVasuGuptaVasuGupta'
>>> str = "Vasu Gupta"
>>> 
>>> 
>>> 


>>> 

>>> 

>>> 

>>> 

>>> 
str[0 , 2]
Traceback (most recent call last):
  File "<pyshell#41>", line 2, in <module>
    str[0 , 2]
TypeError: string indices must be integers
>>> str[0]
'V'
>>> str[-1]
'a'
>>> str[0:4]
'Vasu'
>>> str[0:5]
'Vasu '
>>> str[:4]
'Vasu'
>>> str[:]
'Vasu Gupta'
>>> len(str)
10
>>> players = [23,43,21,14,56,87]
>>> players[0]
23
>>> players[-1]
87
>>> players[0] = 54
>>> players[0]
54
>>> players[0:2]
[54, 43]
>>> players += [66 , 99]
>>> players
[54, 43, 21, 14, 56, 87, 66, 99]
>>> players.appned(120)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    players.appned(120)
AttributeError: 'list' object has no attribute 'appned'
>>> players.append(120)
>>> players
[54, 43, 21, 14, 56, 87, 66, 99, 120]
>>> players.append(140,160)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    players.append(140,160)
TypeError: append() takes exactly one argument (2 given)
>>> players.append([140,160])
>>> players
[54, 43, 21, 14, 56, 87, 66, 99, 120, [140, 160]]
>>> 
players.appned("Hii")
Traceback (most recent call last):
  File "<pyshell#63>", line 2, in <module>
    players.appned("Hii")
AttributeError: 'list' object has no attribute 'appned'
>>> players.append("Hii")
>>> players
[54, 43, 21, 14, 56, 87, 66, 99, 120, [140, 160], 'Hii']
>>> players[:2] = []
>>> players
[21, 14, 56, 87, 66, 99, 120, [140, 160], 'Hii']
>>> hey
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    hey
NameError: name 'hey' is not defined
>>> 
