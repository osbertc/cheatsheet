# Python cheatsheet

<!-- TOC -->

- [Python cheatsheet](#python-cheatsheet)
  - [high-light](#high-light)
  - [Basic](#basic)
  - [Variable, List, Object](#variable-list-object)
  - [String Manipulations](#string-manipulations)
  - [simple math](#simple-math)
  - [comparison operator](#comparison-operator)
  - [if statments](#if-statments)

<!-- /TOC -->

## high-light

| JSON | Python | 
| ---| --- | 
| object | dict | 
| array | list |   
| string | str | 
| number(int) | int | 
| number(real) | float |  
| true | True |  
| false | False | 
| null | None |  


## Basic

```python
print("The \n makes a new line")
print("The \t is a tab")
print('I\'m going to the movies')
print("This is a string enclosed by \"\" not '' ")
```

## Variable, List, Object

variable:
```
var = 'coffees'
```

List:
```python
coffees_list = ['black', 'latte', 'cappuccino', 'espresso', 'mocha', 'flat white', 'irish']
```


Object: 
```python
coffees_price = [
    {'black':{
        'size':['small','regular','large'],
        'price': ['32','39','42']
     }
    },
    {'latte':{
       'size': ['small','regular','large'],
       'price':['32','39','42']
     }
    },
    {'cappuccino':{
       'size': ['small','regular','large'],
       'price':['32','39','42']
     }
    }
  ]
```

## String Manipulations

```python 
 print('hello world')
# basic variable 
var = 'hello world'
print(var)
print(var.lower())
print(var.upper())
print(var.title())
print(var.split(' '))
new_var = ("Fizz" + "Buzz")
```

## simple math

Mathethic Operator | Function
--- | --- 
2+3.4 = 5.4 | sum
130-2.293 = 127.707 | if one of the operands is a float, the result is a float
130.4/2 = 65.2 | division
12*3 = 36 | multiplication
2**3 = 8 | Exponentiation **
29%3 = 2 | Modulo <br> Returns the reainder of the division

## comparison operator

Comparison Operator | Function
--- | --- 
< | less than
<= | less than or equal to
> | greater than
>= | greater than or equal to
== | equal
!= | not equal

## if statments
```python
 
for name in list:
    if name == var:
        pass
    else:
        print(name)
```