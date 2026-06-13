# Data Structure.
# Data structures used to store data efficiently and make faster
# for operation like read and write.
# List
# String
# Dictionary
# Set
# Tuple
# ...........1.List
# 1. List is a data structure in python used to store multiple data in of different types 
# # in one variable.
# 2.List can define by using square [] and data inside known as element.
# 3.List can be heterogenous and homogenous.
# 4.List are mutable (changeable)
# 5. list support indexing ,slicing and follow ordering sequence\
# total index =length-1
# marks_10th=[20, 55,60,76,50,60] #list ke under ke data ko element kehte h
# data=marks_10th[2]
# print(data)
# print("After update: ",marks_10th)

# n=7
# for i in range(n):
#     for j in range(n):
#         if j==0 or j==n-1 or i==n//2:
#             print("*",end= " ")
#         else:
#             print(" ",end=" ")
#     print()

# Slicing
# marks=[10,20,30,40,50,60,70,80,90]
# [start-0:stop-1:step-1]
# sub_list=marks[0:5:2]
# sub2_list=marks[::-1]
# sub3_list=marks[4::-1]
# print(sub_list)
# print(sub2_list)
# print(sub3_list)

# marks=[10,20,30,40,50,60,70,80,90]
# for i in range(len(marks)):
#     if marks[i]%2==0:
#         print(f"This elm is even : {marks[i]}")
#     else:
#         print(f"This elm is odd  : {marks[i]}")  

# marks=[10,20,30,40,50,60,70,80,90]
# total=0
# for i in marks:
#         print(i)
# marks=[10,20,30,40,50,60,70,80,90,100]
# #
# # sub_list=marks[2:9]
# sub_list=marks[:8:-1]
# print(sub_list)      
#wap to swap the first value of the list with last value of the list.

# marks=[10,20,30,40,50,60,70,80,90,100]
# temp=marks[0]
# marks[0]=marks[9]
# marks[9]=temp
# print(marks)

# 1.Wap to find the sum of the all the elements in the List : [10,20,30,40]
# list=[10,20,30,40]
# sum=0
# for i in range(0,len(list)):
#     sum+=list[i]
# print(sum)

# 2.Wap to find the sum of only even elemnts in the list : [10,3,4,6,22,31,33,55,40]
# list=[10,3,4,6,22,31,33,55,40]
# sum=0
# for i in range(0,len(list)):
#     if list[i]%2==0:
#         sum+=list[i]
# print(sum)
# 3.Wap to find the sum of only odd elments in the list : [10,3,4,6,22,31,33,55,40]
# list=[10,3,4,6,22,31,33,55,40]
# sum=0
# for i in range(0,len(list)):
#     if list[i]%2!=0:
#         sum+=list[i]
# print(sum)

# 4.Wap to find the count of how many int value and how many str in the list [70,"aman",50,10,20,"rohan","iq-india"]
# list=[70,"aman",50,10,20,"rohan","iq-india"] 
list=[70,"aman",50,10,20,"rohan","iq-india"]
str_count=0
int_count=0
for i in list:
    if type(i)==int:
        int_count+=1
    elif type(i)==str:
        str_count+=1   
print("Total int Element in the list is : ",int_count)
print("Total Str Element in the List is : ",str_count)    
 
              
            
