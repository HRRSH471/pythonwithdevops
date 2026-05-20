# wap to count the space from the string "This is python"


# str1="This is python"
# count=0  
# for i in str1:             
#     if i==" ":
#       count+=1
# print("Number of spaces in the string:", count)

# Wap to eliminate o and print all string from "How are you"

# str1="How are you"
# result=""
# for i in str1:
#     if i != "o":
#         result += i
# print("String after eliminating 'o':", result)

# wap to cont the number fromt the string "D-1 267/268 Mayur Vihar phase-3 110096"
# address ="D-1 267/268 Mayur Vihar phase-3 110096"
# digit_count = 0
# for i in address:
#  if type(i) == int:
#     digit_count += 1
# print("Number of digits in the address:", digit_count)

# print("Hello Guys My name is Rashi")

# def div(a,b):
#     print(a/b) 
# div(10,20)
# div(30,40)
# div(1,2)

# Waf to check number pass by argument is add or enven
# int_num = int (input("Enter a number: "))
# def check_number(num):
#     # if num % 2 == 0:
#         print(f"{num} is an even number.")
#     else:
#         print(f"{num} is an odd number.")
# check_number(int_num)

# Waf to check which number is greater and two number pass by user

# num1=int(input("Enter first number: "))
# num2=int(input("Enter second number: "))
# def check_greater(num1, num2):
#     if num1 > num2:
#         print(f"{num1} is greater than {num2}.")    
#     elif num2 > num1:
#         print(f"{num2} is greater than {num1}.")
#     else:        
#         print("Both numbers are equal.")
# check_greater(num1, num2)

# Waf to check the character is vowel or consonant

# def check_vowel_consonant(char):
#         i=len(char)-1
#         count_vowel=0
#         count_consonant=0

#         if char[i] in 'aeiouAEIOU':
#             print(f"{char} is a vowel.")
#             count_vowel+=1
#         else:
#             print(f"{char} is a consonant.")
#             count_consonant+=1
# check_vowel_consonant(char)

# Waf to check is number completely divided by 2 and 3 and return
# "Yes Number is completely Divide"
# "NO Number is not completely Divide"
def check_division(num):
    if num % 2 == 0 and num % 3 == 0:
        return "Yes, the number is completely divisible by 2 and 3."
    else:  
        return "No, the number is not completely divisible by 2 and 3."
Answer=check_division(num)
print(Answer)   

# Waf to return length of the string without using len()
# def len_string(s):
#     c=0
#     for i in s:
#         c+=1 
#     return c
# res=len_string("Rashi")
# print(res)

