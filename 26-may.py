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

n=7
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or i==n//2:
            print("*",end= " ")
        else:
            print(" ",end=" ")
    print()





