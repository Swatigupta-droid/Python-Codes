# -*- coding: utf-8 -*-
"""Question3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10lTWIWaMqFWeSRIjpWFnA4pid5H1nEGq

3. Write a Python function to find the nth term of Fibonacci sequence and its factorial. Return the result as a list.
"""

def fact(n):
    f=1
    for x in range(1,n+1):
        f*=x;
    return f
n=int(input("Enter a value "))
print("Factorial : ",fact(n))

def fib(n):
    a = 0
    b = 1
     
    if n < 0:
        print("Incorrect input")

    elif n == 0:
        return 0

    elif n == 1:
        return b
    else:
        for i in range(1, n):
            c = a + b
            a = b
            b = c
        return b
 
def fact(n):
    f=1
    for x in range(1,n+1):
        f*=x;
    return f
n=int(input("Enter the value of n : "))
val=fib(n)
print("The nth element is ",val)
print("The factorial of this number is ",fact(val))