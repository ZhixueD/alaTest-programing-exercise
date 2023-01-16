# alaTest Programing Exercise
This project is for the alaTest challenge 2023, programing exercise.


## Description

Some telephone operators have submitted their price lists including price per minute for different phone number prefixes.
The price lists include two columns. The left column represents the telephone prefix (country + area code) and the right 
column represents the operators price per minute for a number starting with that prefix. When several prefixes match the 
same number, the longest one should be used. 

If a price list does not include a certain prefix you cannot use that operator to dial numbers starting with that prefix.

The Goal:
The goal with this exercise is to write a program that can handle any number of price lists (operators) and then 
can calculate which operator that is cheapest for a certain number. You can assume that each price list can have 
thousands of entries, but they will all fit together in memory.

## Explanation

I create a python file: 'find_lowest_operators.py', which include the class and function to find the cheapest operator.
It also includes a simple test. But for main test, I use python pytest package, and create a python 
file: 'test_find_lowest_operators.py', which include the python script which perform multiple tests 
for 'find_lowest_operators.py'.

The test operators price list, I assume it is a dictionary format. Since dictionary is quite easy to transformed from 
json format, which is quite common used in this kind of problem.



## Getting Started

### Dependencies

* python 3.8, pycharm
* python packages: typing, pytest

### Installing

* install typing, pytest directly from pycharm or using following code
```
pip install typing
```

```
pip install pytest
```

### Executing program

* find_lowest_operators.py contains the class FindOperator, for finding the cheapest operator for certain phone number.
* test_find_lowest_operators.py is the pytest code for run pytest for class FindOperator.


## Authors

Zhixue Du, brantdzx@gmail.com

