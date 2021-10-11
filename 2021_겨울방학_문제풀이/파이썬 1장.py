Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("Hello World!")
Hello World!
>>> 
================ RESTART: C:/Users/201211/Desktop/Hello World.py ===============
Hello World!
>>> a = 20200108
>>> print(a)
20200108
>>> a= str(2020_01_08)
>>> print(a)
20200108
>>> a +1
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    a +1
TypeError: can only concatenate str (not "int") to str
>>> print(a+1)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print(a+1)
TypeError: can only concatenate str (not "int") to str
>>> print(a)
20200108
>>> print(a*2)
2020010820200108
>>> b= int(a)
>>> print(b+1)
20200109
>>> a = 1
>>> b = a + 1
>>> c = a * b
>>> print(a, b, c)
1 2 2
>>> print(a,"X",b,"=",c)
1 X 2 = 2
>>> type(True)
<class 'bool'>
>>> type(false)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    type(false)
NameError: name 'false' is not defined
>>> type(False)
<class 'bool'>
>>> a = 4
>>> b = 4.1
>>> if a == b:
	print("같다.")
	else:
		
SyntaxError: invalid syntax
>>> if a =! b:
	print("같지 않다.")
else:
	print("같다.")
	
SyntaxError: invalid syntax
>>> 
>>> 
>>> if a !! b:
	print("같지 않다.")
else:
	print("같다.")
	
SyntaxError: invalid syntax
>>> if a == b:
	print("같다.")
else:
	print("같지 않다.")

같지 않다.
>>> if type(a) == type(b):
	print("유형이 같다.")
else:
	print("유형이 같지 않다.")

	
유형이 같지 않다.
>>> a = str(2020_01_08)
>>> a = int(2020_01_08)
>>> b = a + 1
>>> print("오늘",a,"내일",b)
오늘 20200108 내일 20200109
'
>>> print("오늘 : ",a,"내일 : ",b)
오늘 :  20200108 내일 :  20200109
>>> 