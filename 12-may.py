#Traversing a string using range() function

# name="python programming"
# size=len(name)
# for i in range(size):
#     print(name[i],i)

# without range() function
# name="python programming"
# for i in name:
#     print(i)

# Var1="DevOps Engineer"
# for i in Var1:
#     if i=="e":
#         continue

#     print(i,end=" ")
# WAP to count all the vowels in the given string: "This is devops batch"

# str1 = "This is devops batch"
# vowels = "aeiouAEIOU"
# v_count=0
# c_count=0
# for char in str1:
#     if char in vowels:
#         count += 1
#     else:
#         c_count += 1

# print("Number of vowels in the string:", v_count)
# print("Number of consonants in the string:",c_count)

# WAp to print your name in regverse formate
# name = input("Enter your name: ")
# reverse_name = ""
# for i in name:
#     reverse_name = i + reverse_name
# print("Your name in reverse format is:", reverse_name, end=" ")

# WAP to sum of the indices of ta string: "python:"
# str1 = "python"
# Count_indices = 0
# for i in range(len(str1)):
#     Count_indices += i
#     print("Sum of indices:", Count_indices)

# # Wap to print the factorial from 1 to 8
# for num in range(1, 9):
#     factorial = 1
#     for i in range(1, num + 1):
#         factorial *= i
#     print(f"Factorial of {num} is: {factorial}")

# Wap to print the only prime numbers from 1 t0 15
# for num in range(1, 16):
#     if num > 1:  # prime numbers are greater than 1
#         for i in range(2, num):
#             if num % i == 0:
#                 break
#         else:
#             print(num)

# Wap to print the only odd numbers from 1 t0 15
# for num in range(1, 16):
#     if num % 2 != 0:  # odd numbers are not divisible by 2                

