# Every Function in python.
# 1. Every function has their own purpose.
# 2. function is block of instruction ( code ) which execute inside its own block
# 3. Funtion is resusable means define one time use manytime (DRY).
# 4. Function has two main part first funtion defination second function calling.
# 5. in python bydefault function retuns None if we not return anything.


# How define function in python.
# def add(): # (): We call it parameter at time of calling function
#     a = 10
#     b = 20
#     c = a + b
#     print(c)
# How to call function in python.
# add() # () we call it arguments at time of calling function

# Function define into four category.
# 1. Take nothing return nothing.
# 2. Take nothing return something.
# 3. Take something return nothing
# 4. Take something return something

# Parameters (Para) and arguments(agrs
# Positional parameter/arguments
# Default parameter (a=0, b=0)
# def table_print(n):
#     for i in range(1, 11):
#         print(f"{n} x {i} = {n*i}")
# table_print(5) # 5 is argument 
# print()
# table_print (7) # 7 is argument
# print()   

# # function to Add two number
# def add(a,b, c=0):
#     print("Addition :",a+b+c) 
# add(10, 20)

# # function to Subtract two number
# def sub(a=0,b=0):
#     print("Subtraction :",a-b)
# sub(20, 10)

# # function to Multiply two number
# def mul(a=0,b=0):
#     print("Multiplication :",a*b)
# mul(10, 20)

# #function to divide two number
# def div(a=0,b=0):
#     print("Division :",a/b)  
# div(20, 10)

# num1=int(input("Enter first number :"))
# num2=int(input("Enter second number :"))
# opt=input("Choose option : +, -, *, /")
# if opt == "+":
#     add(num1, num2)
# elif opt == "-":
#     sub(num1, num2)
# elif opt == "*":
#     mul(num1, num2)
# elif opt == "/":
#     div(num1, num2)
# else:
#     print("shi se input")  

# def add(a, b):
#     return a + b # we can return any type of data like int, str, list, tuple, dict etc.
# res=add(2,3)
# print(res-5)

# def greet(a):
#      return a
# g=greet("Hello")

# def user_name(b):
#     return b
# u=user_name("Rohit")
# print(g, u)

# Waf to check given how many vowel in a given string.


def vowel_count(a):
    c=0
    for i in a:
        if i in "aeiou":
         c+=1
    return c
res=vowel_count("Programming")    

# local Variable vs Global Variable  
# name="Dev" #global variable
# def msg():
#     global name  #now vaiable become global inside the function
#     name="Hariom" # Local Variable
#     print(name)
# msg()
# print(name)  

# Waf to count char "p" in python programing 

# def count_p(a):
#     c=0
#     for i in a:
#         if i == "p":
#          c+=1
#     return c
# res=count_p("python programming")
# print(res)

# def vowel_count (dest,find):
#    c=0
#    for in in dest:
#       if i == find:
#          c+=1
#     return c
# dest="python programing"
# find= "n"
# res=vowel_count(dest,find)
# print(res)

#Waf to return sum of strings indexes.
# def sum_indices(a):
#     str1="python"
#     sum=0
#     for i in range (len(a)):
#         sum+=i
#     return sum
# res=sum_indices("python")
# print(res)



