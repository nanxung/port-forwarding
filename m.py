#!/usr/bin/python2
#coding:utf8
a = input('number:')
count=0
while a>1:
    if a%2:
        a=a/2
    else:
        a=a*3+1
    count=count+1
    print a,count

