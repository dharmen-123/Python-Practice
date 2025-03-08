#print("HELLO WORLD")
# print('dharmendra')

       # Data types and variables
# a=input('enter the value of a : ')
# b=input('enter the value of b : ')
# hello= a
# a=b
# b=hello
# print("The value of a is = " + a)
# print("The value of b is = " + b)
# /

# def myfunc():
#   global x
#   x = "fantastic"

# myfunc()

# print("Python is " + x)
          #    How to define type of any variable
# condition = True
# name = "dharmendra"
# print(type(condition))
# print(type(name))
# age = 24
# condition = True
# numbeer = 24.45
# print(type(age))
# print(type(condition))
# print(type(numbeer))
        # how to swap two nunbers
# a = input("enter value of a :")
# b = input("enter value of b :")
# right = a
# a=b
# b= right
# print(a)
# print(b)
# age = int(input("Enter the age :"))
# if (age>=18):
#      print("You are not audult ")
# else :
#     print("You are audult ")
# # print("Thanks")
       # Global Variables
# def myfunc():
#   global x
#   x = "fantastic"

# myfunc()

# # print("Python is " + x)
# x = "hello"
# x = "fantastic"
# def myfunc():
#   global x 
#   x = "awesome"  
#   myfunc()
# print("Python is " + x)
#       #Arithmetic operators
# a = 6
# b = 3
# print(a+b) additon
# print(a-b) subtraction
# print(a*b)multiplication
# print(a/b) division
# print(a%b) modulus
# print(a**b)  exponential
# print(a//b)  floor division

#       #Relational Operators
# a = 6
# b = 3
# print("print right condition")
# print(a==b) equal to equal to
# print(a!=b) 
# print(a>=b) greater then equal
# print(a<=b) less than equal
# print(a>b) greater than
# print(a<b) less than
   # Bitwise operators
# a=5
# b=4
# print(a&b)  And operators
# print(a|b) Or operators
# print(a^b) Xor operators
# print(~b)  Not operators
# print(a<<b)  Left shift operators
# print(a>>b)  Right shift operators
      #assignment Operators
# num= 10
# num+=12
# num-=5
# num/=28
# num*=6
# num%=7
# print("num :",num)
        #logical Operators
# print(not False)
# print(not True) 
# s1=int(input("Enter first value: "))
# s2=int(input("Enter second value: "))
# s3=int(input("Enter third value: "))
# if (s1==s2 and s2==s3 and s3==s1):
#     { print("It is equalaterial Triangle")
#     }
# elif (s1==s2 or s2==s3 or s3==s1):
#     {
#      print("It is isoscales Triangle")
#     }
# else :
#     {
#      print("It is scalene Triangle")
#     }
       #     list is the ordered collection of data with element
# list = (4,6,-3,-6,"apple,grapes")
# print(list)
   #   tuple is also an ordered collection of data with element but it is immutable
# tuple= ("parrat","bird",("lion","tiger"))
# print(tuple)
# print(2**4)
# print(4%2)
# print(23//5)
# print(36/7)

#                      THIS IS SIMPLE CALCULATOR
# print("This is a simple calculator")
# print("Enter 1 for addition")
# print("Enter 2 for subtraction")
# print("Enter 3 for multiply")
# print("Enter 4 for division")
# operators = input("Enter the choice :")
# a = int(input('Enter the first value : '))
# b = int(input('Enter the second value : '))
# if operators=='1':
#   print('The answer is :' , a+b)
# elif operators=='2':
#   print('The answer is :' , a-b)
# elif operators=='3':
#    print('The answer is :', a*b)
# elif operators=='4':
#   print('The answer is :' , a/b)
# else:
#   print("you have selected  not proper choice")
# print('hello')
#             #type casting
# length = len("Dharmendra chilhate")
# print("your name has "+str(length)+" characters")
# firstno = input("enter 1st no.")
# secondno = input("enter 2nd  no.")
# sum = int(firstno)+int(secondno)
# print("sum is : ",sum)
#      Round Fuction
# number= 2.6899
# print(round(number))
# print(round(11.4))
# print(round(12.5))
      # F-- Strings
# name = 'Dharmendra Chilhate'
# age = 19
# height = 5.8
# print(f"My name is {name} I am {age} years old. My height is {height} meters")
# import math
# x= math.sqrt(25)
# print(x)   
# print(math.pow(3,2))
# name = "Dharmendra"
# for characters in name:
#     print(characters)
 # DIFFRENT TYPES OF STAR  PATTERN 
  # rectangular star pattern
# n= int(input('Enter the number : '))      * * * * 
# for i in range(0,n):                      * * * *
#     for j in range(0,n):                  * * * *
#         print('*  ',end="  ")             * * * *
#     print( )  
 #  triangle pattern
# n=6
# for i in range(n):
#      for j in range(i,n):
#           print('*',end="  ")
#      for j in range(i+1):
#           print('*',end="  ")
#      print()   
    # hill pattern

# for i in range(n):
#      for j in range(i,n):
#           print('',end="  ")
#      for j in range(i+1):
#           print('* ',end="  ")
#      for j in range(n):
#           print('*',end="  ")
#      print()   
# r=5                            *
# for i in range (r):            * *           
#     for j in range(i+1):       * * *
#        print(' * ',end=" ")    * * * * 
#     print()                    * * * * *       
# r=5                                   * * * * *
# for i in range(r):                    * * * *
#        for j in range(r-i):           * * *
#               print('* ',end=" ")     * *
#        print()                        *
#          0 
#          0 1
#          0 1 2
#          0 1 2 3
#          0 1 2 3 4
# n=5                                    
# for i in range(0,5):
#        for j in range(0,i+1):
#               print(j ,end=" ")
#        print()  
#         5 4 3 2 1 
#         4 3 2 1
#         3 2 1
#         2 1
#         1
# n=5
# for i in range(n,0,-1):
#        for j in range(i,0,-1):
#               print(j,end=" ")
#        print()

# n=5
# for i in range(n):
#     for j in range(i+1):
#        print(' ',end=" ")
#     for j in range(1,i+1):
#        print('*',end=" ")   
#     for j in range(n):
#        print('*',end=" ")   
#     print()


     # STRING AS AN ARRAY
# names = "DHARMENDRA CHILHATE"
# print(len(names))
# len1= len(names)
#  print("names is a ",len1 ,"character")
# fruit = "Mango"
# len1=len(fruit)
# print(len1)
# print(fruit[0:4])
# print(fruit[1:4])
# print(fruit[:5])
# print(fruit[0:len(fruit)-3])
# num = "dharmendra"
# print(num[-4:-2])

#              #STRINGS ARE IMMUTABLE
#  a="Dharmendra"
# print(len(a))
# print(a.lower())    #lower method
# print(a.upper())    #upper method
# print(a.rstrip("dra"))
# print(a.lstrip("Dha"))
# print(a.replace("Dharmendra","Chanchal"))
# lst= "my name is dharmendra CHILHATE"
# print(lst.capitalize())
# # print(a.split())
# name="hello python and python is easy language"
# print(len(name))
# print(name.count("python"))
# print(name.endswith("language"))
# print(name.endswith("and",10,16))
# print(name.find("and"))
# password=(input("enter : "))
# if password == "Dharmendra@123":
#    print("correct password")
# else:
#    print("Wrong password \n Try again")
# String methods for check conditions
# isalnum ,isalpha ,islower ,isprintable
# isspace ,istitle ,startswith
# str1="his name is python."
# print(str1.title())
# print(str1.capitalize())
# print(str1.isupper())
# print(str1.islower())
# print(str1.replace("his","Their"))
# print(str1.startswith("his"))
      
        # CONDITIONAL STATEMENTS  #
# IF   # IF-ELSE  # IF-ELSE-ELIF     # NESTED IF ELSE
# conditional operators
# ==   # !=   # >   # <   # >=   # <=
# a=int(input("Enter the age: "))
# print("Your age is", a)
# if a>=18:
#    print("You are adult")
#    print("You are eligible for voting")
# else:
#    print("You are not eligible for voting")
# num = int(input("Enter the number"))
# if num < 0:
#        print("Number is negative")
# elif num==0:
#        print("Number is zero")
# else:
#        print("Number is positive")
# print("elif condition is done")
# import time
# print("Good Morning")
# sleep(1)
# print("Good Morning Sir")
# sleep(2)
# print("How are you")
# sleep(1)
# print("I am fine")
# sleep(2)
# print("What is going on")
# sleep(1)
# print("Coding")
# times=time.strftime('%H,%M,%S')
# print(times)
# ct=time.time()
# print(ct)
# localt=time.localtime(ct)
# print(localt)
# print(time.ctime(ct))
"""In C++ use switch  case statement but in python we use match  case statement
 in this case if any one case is  true than next statement is not check program
  is done match does not check other case and also it does not break statement
   like C++ without break statement program will check cases"""
x=int(input("Enter value"))
match x:
       case 0:
            print("x is zero")
       case 4:
            print("case is 4")
       case _:
            print(x)
             # LOOPING STATEMENTS
# set1={1,2,"hello",4.56,"A",3029}
# set2={1,2,7,9,5,6}
# for i in set1:
#     print(i , end=" ")
# print(set2)
# a1=5
# for i in range(a1):
#     for j in range (i-1):
#          print("*",end=" ")
#     print()
 