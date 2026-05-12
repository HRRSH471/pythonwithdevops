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
name = input("Enter your name: ")
reverse_name = ""
for i in name:
    reverse_name = i + reverse_name
print("Your name in reverse format is:", reverse_name, end=" ")