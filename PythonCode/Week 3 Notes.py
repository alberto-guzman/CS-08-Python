Python 3.5.1 |Anaconda 4.0.0 (x86_64)| (default, Dec  7 2015, 11:24:55)
[GCC 4.2.1 (Apple Inc. build 5577)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> total = 5/2
>>> type(total)
<class 'float'>
>>> print(2.3 + 4.7)
7.0
>>> if True:
... print(5)
  File "<stdin>", line 2
    print(5)
        ^
IndentationError: expected an indented block
>>> if True:
...     print(5)
...
5
>>> if False:
...     pront(5)
...
>>> if False and False:
...     print("and is True")
...
>>> if False and True:
...     print("and is True")
...
>>> balance = 100
>>> ift balance > 0 and int(input("how much?"))<= balance:
  File "<stdin>", line 1
    ift balance > 0 and int(input("how much?"))<= balance:
              ^
SyntaxError: invalid syntax
>>> if balance > 0 and int(input("how much?"))<= balance:
...     print("transfer allowed")
...
how much?50
transfer allowed
>>> balance = -5
>>> if balance > 0 and int(input("how much?"))<= balance:
...     print("transfer allowed")
...
>>> balance >0
False
>>> has_money = balance>0
>>> has_money
False
>>> print(has_money)
False
>>> if has_money:
...     print("you have money")
...
>>> #change balance to 1000
... balance=1000
>>> #did it detect the new balance?
... print(has_money)
False
>>> #it did not
... has_money = balance>0
>>> print(has_money)
True
>>> #not its updated
...
>>> a=5
>>> b=10
>>> c = a + b
>>> c
15
>>> a = 0
>>> b=-10
>>> c
15
>>> 7 == 7.0
True
>>> 7 == 6.33333 + .66666
False
>>>  6.33333 + .66666
  File "<stdin>", line 1
    6.33333 + .66666
    ^
IndentationError: unexpected indent
>>>  6.33333 + .66666
  File "<stdin>", line 1
    6.33333 + .66666
    ^
IndentationError: unexpected indent
>>> (6 + 1/3) + (2/3) == 7
True
>>> #rounding errors
...
>>> #floating point values end up with rounding error
...
>>> a = 5.2
>>> b = 3.987
>>> a+b
9.187000000000001
>>> a+b == 9.187000000000001
True
>>> a+b == 9.187
False
>>> #roudning error
...
>>> a + b > 9
True
>>> a + b > '9'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unorderable types: float() > str()
>>> # cant compare a float and a string
...
>>> a + b > int('9')
True
>>> 'this' ==
  File "<stdin>", line 1
    'this' ==
             ^
SyntaxError: invalid syntax
>>> 'this' == 'this'
True
>>> 'this' == "this"
True
>>> 'this' == 'This'
False
>>> #case senesitive comparison
...
>>> 'this'>'This'
True
>>> 'a' >= 'b'
False
>>> 'a' < 'b'
True
>>> 'g'>'h'
False
>>> 'g'=='h'
False
>>> 'g' < 'h'
True
>>> #what its doing is converting the letter into a binary into ASCII or unicode
...
>>> type(g)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'g' is not defined
>>> #doing everything in terms of letter order, upper case letters come first
...
>>>






#Rouletter Wheel example


