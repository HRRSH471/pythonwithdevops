# start_num=int(input("Enter the the starting number : "))
# End_num=int(input("Enter the the End Number : "))
# sum=0
# for i in range(start_num+1,End_num):
#     sum+=start_num
#     print(sum)
# def square(n):
#     sqr=n*n
#     return sqr

# def greet(name):
#     return "Hello " + name

# msg = greet("Hariom")
# print(msg)

# def check_even(num):
#     if num % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"
# res = check_even(int(input("Enter the Number : ")))
# print(res)

# def area_triangle(base, height):
#     area = 1/2 * base * height
#     return area

# result = area_triangle(int(input("Enter the Base of Trianle")), int(input("Enter the Hight of the Triangle")))
# print(result)

# def add():
#     a = int(input("Enter first number: "))
#     b = int(input("Enter second number: "))

#     return a + b

# result = add()
# print(result)

# def multiply():
#     a = int(input("Enter first number: "))
#     b = int(input("Enter second number: "))

#     return a * b

# result = multiply()
# print(result)

# def hello():
#     return "Hello"
# res=hello()
# print(res) 

# def hello():
#     return "Hello"

# print(hello())
# def message(text):
#     return text


# msg = input("Enter any string: ")

# result = message(msg)

# print(result)

# def reverse_string(name):

#     reverse = ""

#     for i in name:
#         reverse = i + reverse

#     return reverse


# name = input("Enter a string: ")

# result = reverse_string(name)

# print(result)

text = input("Enter a string: ")

reverse = text[::-1]

print(reverse)