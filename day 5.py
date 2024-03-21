# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 10:03:41 2024

@author: Admin
"""

def reciprocal( num1 ):
    try:
        reci = 1 / num1
    except ZeroDivisionError:
            print("we cannot divide by zero")
    else:
        print( reci )
reciprocal( 4 )
reciprocal( 0 )


a = ["python", "exception", "try and except"]
try:
    for i in range(4):
        print("the index and element from the array is",i,a[i])
except:
    print("Index out of range")
    
    
try:
    1/0
except Exception:
    print("Exception")
except ZeroDivisionError:
    print("Zero Divison")

class test(Exception):
    pass
class test1:
    a=[11,12,21,24]
    def check(self,id):
      s=0
      for i in self.a:
       if(id==i):
        s=1
        break
      if(s!=0):
       return True
      else:
        raise test
try:
  account1=test1()
  account1.check(14)
  print("found")
except test:
  print("not found")     


class person:
    def __init__(self,voter_list):
        self.__voter_list=voter_list
    def check_person(self,person_id):
        try:
            if person_id not in self.__voter_list:
                raise Exception
                print("1")
        except Exception:
                print("2")
obj1=person([1001,1002,1003])
obj1.check_person(1005)
print("3")
                
class person:
    def __init__(self,voter_list):
        self.__voter_list=voter_list
    def check_person(self,person_id):
        try:
            if person_id not in self.__voter_list:
                raise Exception
                print("1")
        except Exception:
                print("2")
obj1=person([1001,1002,1003])
obj1.check_person(1005)
print("3")
        

class 