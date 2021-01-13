# Python cheatsheet

<!-- TOC -->

- [Python cheatsheet](#python-cheatsheet)
  - [High-light](#high-light)
  - [Basic](#basic)
  - [Variable, List, Object](#variable-list-object)
  - [Operators](#operators)
    - [Mathethic Operator](#mathethic-operator)
    - [Comparison operator](#comparison-operator)
    - [Logical Operator](#logical-operator)
  - [String Manipulations](#string-manipulations)
  - [if, else statments](#if-else-statments)

<!-- /TOC -->

## High-light

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

## Operators

### Mathethic Operator

Mathethic Operator | Function
--- | --- 
2+3.4 = 5.4 | sum
130-2.293 = 127.707 | if one of the operands is a float, the result is a float
130.4/2 = 65.2 | division
12*3 = 36 | multiplication
2**3 = 8 | Exponentiation **
29%3 = 2 | Modulo <br> Returns the reainder of the division



### Comparison operator

Comparison Operator | Function
--- | --- 
< | less than
<= | less than or equal to
> | greater than
>= | greater than or equal to
== | equal
!= | not equal

### Logical Operator

Logical Operator | Description
--- | ---
and | If both the operands are True then condition becomes True.
or | If any of the two operands are True then condition becomes True. 
not | Used to reverse the logical (not False becomes True, not True becomes False)

## String Manipulations

```python 
var = 'regular latte'
print(var)
print(var.lower())
print(var.upper())
print(var.title())
print(var.split(' '))
new_var = ("large" + "mocha")
```

## if, else statments
```python
order = 'latte'  # customer place order
coffees_list = ['black', 'latte', 'cappuccino', 'espresso', 'mocha', 'flat white', 'irish']  # our shop's product list
for coffee in coffees_list: 
    if coffee != order: 
        pass # pass if order not match list
    else:
        print('Our Coffee list have customer\'s perfered coffee')
```

