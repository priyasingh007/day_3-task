#!/usr/bin/env python
# coding: utf-8

# In[8]:


#Functions in Python
#A function in Python is an aggregation of related statements designed to perform a computational, logical, or evaluative task.
#Functions can be both built-in or user-defined. It helps the program to be concise, non-repetitive, and organized.
# A function prog to check even and odd
 
 #example:
def my_function():
  print("I'm function")
my_function()


# In[7]:


def hello():
    print("Hello")
hello()


# In[9]:


# max function to find greatest no:
def max_of_two( x, y ):
    if x > y:
        return x
    return y
def max_of_three( x, y, z ):
    return max_of_two( x, max_of_two( y, z ) )
print(max_of_three(3, 6, -5))


# In[10]:


#ques 2:
def multiply(numbers):  
    total = 1
    for x in numbers:
        total *= x  
    return total  
print(multiply((8, 2, 3, -1, 7)))


# In[11]:


# reverse string:
def string_reverse(str1):

    rstr1 = ''
    index = len(str1)
    while index > 0:
        rstr1 += str1[ index - 1 ]
        index = index - 1
    return rstr1
print(string_reverse('1234abcd'))


# In[13]:


#nested function
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("Input a number to compute the factiorial : "))
print(factorial(n))


# In[14]:


#argument calling
#user defined fumction
def sum (a,b):    
    return a+b;     
a = int(input("Enter a: "))    
b = int(input("Enter b: "))    
  
print("Sum = ",sum(a,b))    


# In[15]:


#required armunent
def func(name):    
    message = "Hi "+name  
    return message  
name = input("Enter the name:")    
print(func(name))    


# In[16]:


#default argument
def printme(name,age=22):    
    print("My name is",name,"and age is",age)    
printme(name = "PRIYA")


# In[17]:


#variable length argument
def printme(*names):    
    print("type of passed argument is ",type(names))    
    print("printing the passed arguments...")    
    for name in names:    
        print(name)    
printme("PRIYA","AMAN","internity","data science")


# In[8]:


#modules
#A module is a file containing Python definitions and statements. A module can define functions, classes, and variables. 
# A simple module, calc.py# importing sqrt() and factorial from the
# module math
from math import sqrt, factorial

print(sqrt(16))
print(factorial(6))


# In[10]:


#  Import built-in module  random
from random import *
 
print(dir(random))


# In[11]:


#  Import built-in module  random
import  random
print(dir(random))


# In[12]:


# importing built-in module math
import math
 
# using square root(sqrt) function contained
# in math module
print(math.sqrt(25))
 
# using pi function contained in math module
print(math.pi)
 
# 2 radians = 114.59 degreees
print(math.degrees(2)) 
 
# 60 degrees = 1.04 radians
print(math.radians(60)) 
 
# Sine of 2 radians
print(math.sin(2)) 
 
# Cosine of 0.5 radians
print(math.cos(0.5)) 
 
# Tangent of 0.23 radians
print(math.tan(0.23))
 
# 1 * 2 * 3 * 4 = 24
print(math.factorial(4)) 
 
# importing built in module random
import random
 
# printing random integer between 0 and 5
print(random.randint(0, 5)) 
 
# print random floating point number between 0 and 1
print(random.random()) 
 
# random number between 0 and 100
print(random.random() * 100) 
 
List = [1, 4, True, 800, "python", 27, "hello"]
 
# using choice function in random module for choosing
# a random element from a set such as a list
print(random.choice(List))
 
 
# importing built in module datetime
import datetime
from datetime import date
import time
 
# Returns the number of seconds since the
# Unix Epoch, January 1st 1970
print(time.time()) 
 
# Converts a number of seconds to a date object
print(date.fromtimestamp(454554)) 


# In[13]:


#Python – List Comprehension
#syntax : newList = [ expression(element) for element in oldList if condition ]
# Empty list
List = []

for character in 'hello there 16!':
    List.append(character)
 
# Display list
print(List)


# In[14]:


# Using list comprehension to iterate through loop
List = [character for character in 'hello there 16!']
 
# Displaying list
print(List)


# In[15]:


#nested list 
matrix = []
 
for i in range(3):
    
    matrix.append([])
     
    for j in range(5):
        matrix[i].append(j)
         
print(matrix)


# In[16]:


# Nested list comprehension
matrix = [[j for j in range(5)] for i in range(3)]
 
print(matrix)


# In[17]:


# using lambda to print table of 5
numbers = []
 
for i in range(1, 6):
    numbers.append(i*10)
 
print(numbers)


# In[18]:


#iterator
#1.The iterator object is initialized using the iter() method. It uses the next() method for iteration.
#An iterable object is an object that implements __iter__, which is expected to return an iterator object
#2.Why do we use iterator in python?
#Iterators allow lazy evaluation, only generating the next element of an iterable object when requested. This is useful for very large data sets. 
#3.Return an iterator from a tuple, and print each value:

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))


# In[19]:


#Strings are also iterable objects, containing a sequence of characters:

mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))


# In[20]:


#Looping Through an Iterator
mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)


# In[21]:


#generator
#1. what is generator function in python:
#Generator-Function : A generator-function is defined like a normal function, but whenever
#it needs to generate a value, it does so with the yield keyword rather than return. 
#2.Generators with Iterators
def generator_thr_iter():
   yield 'xyz'
   yield 246
   yield 40.50
for i in generator_thr_iter():
   print(i)


# In[ ]:




