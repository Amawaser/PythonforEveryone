Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print('hello world')
hello world
>>> print('hello loong')
hello loong
>>> name = 'Amawasee'
>>> last name = 'Rukruang'
SyntaxError: invalid syntax
>>> lastname = 'Rukruang'
>>> fullname = name + ' ' + lastname
>>> print(fullname)
Amawasee Rukruang
>>> fullname = name + lastname
>>> print (fullname)
AmawaseeRukruang
>>> fullname = name + ' ' + lastname
>>> print(fullname)
Amawasee Rukruang
>>> fullname=name+' '+lastname
>>> print(fullname)
Amawasee Rukruang
>>> type(name)
<class 'str'>
>>> age = 39
>>> type(age)
<class 'int'>
>>> print(type(age))
<class 'int'>
>>> number = 1
>>> number.zfill(3)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    number.zfill(3)
AttributeError: 'int' object has no attribute 'zfill'
>>> number = '1'
>>> number.zfill(2)
'01'
>>> print('ลุงครับผมชื่อ{} นามสกุล{} อายุ{} ขวบ'.format(name,lastname,age))
ลุงครับผมชื่อAmawasee นามสกุลRukruang อายุ39 ขวบ
