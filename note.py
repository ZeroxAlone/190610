# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 15:42:24 2019

@author: translucky
"""
'''
a=1
b=2
def switch(x,y):
    n=y
    y=x
    return n,y
a,b=switch(a,b)
print(a,b)

a=1
b=2
def switch2(x,y):
    tmp=x
    x=y
    y=tmp
    return x,y
print(a,b)
a,b=switch2(a,b)
print(a,b)


def func(Grade,Class,Name):
    return "{}{}-{}".format(Grade,Class,Name)
'''
n=int(input("please input a num:"))
a=0
b=1
i=0
while i<n:
    a,b=b,a+b
    i+=1
if i==n:
    print(a)

def fib(n):
    if n==0 or n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
print(fib(n-1))

m=int(input("please input a number:"))
a=0
b=1
i=0
while a<n:
    a,b=b,a+b
if a==n:
    print("Yes")
else:
    print("No")