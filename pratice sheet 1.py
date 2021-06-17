Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
============== RESTART: D:/ML-summer training/practice sheet 1.py ==============
>>> 
============== RESTART: D:/ML-summer training/practice sheet 1.py ==============
>>> 5**9
1953125
>>> 3//2
1
>>> 7//3
2
>>> 7/3
2.3333333333333335
>>> 6 == 6
True
>>> a = 20
>>> a += 30
>>> a %= 3
>>> print(a)
2
>>> True * False
0
>>> True & False
False
>>> True and False
False
>>> ((6>3) and (7<4) or (18==3)) and (9>3)

False
>>> True is False
False
>>> 
KeyboardInterrupt
>>> False in ‘False’

SyntaxError: invalid character '‘' (U+2018)
>>> False in 'False'
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    False in 'False'
TypeError: 'in <string>' requires string as left operand, not bool
>>> ((True == False) or (False > True)) and (False <= True)

False
>>> 
>>> 
>>> ### 3.
>>> s1 = "Nice to have it"
>>> s2 = " here"
>>> s1 + s2
'Nice to have it here'
>>> s2 = "here"
>>> s1+''+s2
'Nice to have ithere'
>>> s1+{''}+s2
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    s1+{''}+s2
TypeError: can only concatenate str (not "set") to str
>>> s = s1 + s2[:14]+' '+ s1 + s2[14:]
>>> s
'Nice to have ithere Nice to have it'
>>> s = [s1 + s2][:14]+' '+ [s1 + s2][14:]
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    s = [s1 + s2][:14]+' '+ [s1 + s2][14:]
TypeError: can only concatenate list (not "str") to list
>>> s = ['s1 + s2'][:14]+' '+ ['s1 + s2'][14:]
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    s = ['s1 + s2'][:14]+' '+ ['s1 + s2'][14:]
TypeError: can only concatenate list (not "str") to list
>>> s1 + ' ' + s2
'Nice to have it here'
>>> 
>>> 
>>> 
>>> 
>>> #### 4.
>>> a = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]

>>> a = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
>>> a[3][1][2]
['hello']
>>> print(a)
[1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7]
>>> a[3][1][2]
['hello']
>>> 
>>> 
>>> 
>>> ##### 5.
>>> a = s1 + a[:5] + s2
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    a = s1 + a[:5] + s2
TypeError: can only concatenate str (not "list") to str
>>> type(a)
<class 'list'>
>>> str(a)
"[1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7]"
>>> a = s1 + a[:5] + s2
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    a = s1 + a[:5] + s2
TypeError: can only concatenate str (not "list") to str
>>> a += s1
>>> a
[1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7, 'N', 'i', 'c', 'e', ' ', 't', 'o', ' ', 'h', 'a', 'v', 'e', ' ', 'i', 't']
>>> a += [s1]
>>> a
[1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7, 'N', 'i', 'c', 'e', ' ', 't', 'o', ' ', 'h', 'a', 'v', 'e', ' ', 'i', 't', 'Nice to have it']
>>> a = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
>>> a
[1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7]
>>> a += [s1]
>>> a
[1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7, 'Nice to have it']
>>> a += [s2]
>>> a
[1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7, 'Nice to have it', 'here']
>>> print([s1]+a+[s2])
['Nice to have it', 1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7, 'Nice to have it', 'here', 'here']
>>> a = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
>>> print([s1] + a + [s2])
['Nice to have it', 1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7, 'here']
>>> 
>>> 
>>> 
>>> ###### 6.
>>> color_list_1 = set(["White", "Black", "Red"])
>>> color_list_2 = set(["Red" "Green"])
>>> color_list_2 = set(["Red", "Green"])
>>> color_list_1 - color_list_2
{'White', 'Black'}
>>> my_set = print([color_list_1 - color_list_2])
[{'White', 'Black'}]
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> ####### 7.
>>> o = input('Write any sentence')
Write any sentenceMy name is Manikanta
>>> 
==================== RESTART: D:/ML-summer training/practice sheet 1.py ====================
Write your nameManikanta
Traceback (most recent call last):
  File "D:/ML-summer training/practice sheet 1.py", line 15, in <module>
    if(ispangram(o) == True):
NameError: name 'ispangram' is not defined
>>> 
==================== RESTART: D:/ML-summer training/practice sheet 1.py ====================
Yes
>>> 
==================== RESTART: D:/ML-summer training/practice sheet 1.py ====================
Enter your name Manikanta
Traceback (most recent call last):
  File "D:/ML-summer training/practice sheet 1.py", line 29, in <module>
    if(ispangram(string) == True):
NameError: name 'string' is not defined
>>> 
==================== RESTART: D:/ML-summer training/practice sheet 1.py ====================
Enter your name Manikanta
No
>>> 
==================== RESTART: D:/ML-summer training/practice sheet 1.py ====================
Enter your name Hello today was the day 
No
>>> 
==================== RESTART: D:/ML-summer training/practice sheet 1.py ====================
Enter your name Dracula
Traceback (most recent call last):
  File "D:/ML-summer training/practice sheet 1.py", line 29, in <module>
    if(ispangram(s) == True):
NameError: name 'ispangram' is not defined
>>> 
==================== RESTART: D:/ML-summer training/practice sheet 1.py ====================
Enter your name manikanta
No
>>> 
==================== RESTART: D:/ML-summer training/practice sheet 1.py ====================
Enter your name manikanta
No
>>> 
==================== RESTART: D:/ML-summer training/practice sheet 1.py ====================
Enter your name 'manikanta'
No
>>> 
==================== RESTART: D:/ML-summer training/practice sheet 1.py ====================
Pangram
>>> 
==================== RESTART: D:/ML-summer training/practice sheet 1.py ====================
Pangram
>>> 
==================== RESTART: D:/ML-summer training/practice sheet 1.py ====================
Enter your namemanikanta
Not Pangram
>>> type(s)
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    type(s)
NameError: name 's' is not defined
>>> type(st)
<class 'str'>
>>> 
==================== RESTART: D:/ML-summer training/practice sheet 1.py ====================
Enter your namethe walk around here was cooler
Not Pangram
>>> 
==================== RESTART: D:/ML-summer training/practice sheet 1.py ====================
Enter your nameThe quick brown fox jumps over the lazy dog
Pangram
>>> 
==================== RESTART: D:/ML-summer training/practice sheet 1.py ====================
Enter your nameThe quick brown fox jumps over 
Not Pangram
>>> 
==================== RESTART: D:/ML-summer training/practice sheet 1.py ====================
Enter your namethe the 
Not Pangram
>>> 
>>> 

>>> 




>>> 

>>> 


>>> 



>>> 

>>> 




>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> ######## 8.
>>> eval('{0
     
SyntaxError: EOL while scanning string literal
>>> eval('{0}+{0}{0}+{0}{0}{0}'.format(input('Enter the number: ')))
Enter the number: 5
615
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> ######### 9.
>>> sen = ' without,hello,bag,world'
>>> sen
' without,hello,bag,world'
>>> sen[0]
' '
>>> sen = 'without,hello,bag,world'
>>> sen
'without,hello,bag,world'
>>> sen[0]
'w'
>>> sen = ['without'],['hello'],['bag'],['world']
>>> sen[0]
['without']
>>> sen.sort()
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    sen.sort()
AttributeError: 'tuple' object has no attribute 'sort'
>>> sen = ['without','hello','bag','world']
>>> sen.sort()
>>> print(sen)
['bag', 'hello', 'without', 'world']
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> ########### 10.
>>> 
>>> d = {'Student':['Rahul', 'Kishore', 'Vidhya', 'Raakhi'],'Marks': [57,87,67,79]}
>>> d['Marks']
[57, 87, 67, 79]
>>> max(d['Marks'])
87
>>> max(d['Marks']['Student'])
Traceback (most recent call last):
  File "<pyshell#139>", line 1, in <module>
    max(d['Marks']['Student'])
TypeError: list indices must be integers or slices, not str
>>> 
