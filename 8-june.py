# 7. In-built methods in Python

# insert() method is used to add an element at a specific position in the list.
# append() method is used to add an element at the end of the list.
# extend() method is used to add all the elements of a list to another list.
# index() method is used to find the index of the first occurrence of an element in the list.

emp_list=[]
for i in range (1,10):
    name=input("Enter the employee name: ")
    emp_list.append(name)
print(emp_list)

# clear() method is used to remove all the elements from the list.
# pop() method is used to remove an element from the list based on the index.
# remove() method is used to remove an element from the list based on the value.
# my_list=[1,2,3,4,5]
# r1=my_list.remove(2) # removes the element at index 2 (which is 3)
# print(my_list) # Output: [1, 2, 4, 5]
# sort() method is used to sort the elements of the list in ascending order.
# my_list=[10,2,33,4,500,600]
# my_list.sort()
print(my_list) # Output: [2, 4, 10, 33, 500, 600]
# reverse() method is used to reverse the order of the elements in the list.
# my_list=[5,4,3,2,1]
# my_list.reverse()
print(my_list) # Output: [1, 2, 3, 4, 5]
#copy() method is used to create a copy of the list.
# my_list=[1,2,3,4,5]
# new_list=my_list.copy()
# print(new_list) # Output: [1, 2, 3, 4, 5]
# print(new_list is my_list) # Output: False (new_list is a different object than my_list)

#count() method is used to count the number of occurrences of an element in the list.
# my_list=[100,200,300,400,500]
# res=my_list.count(300)
# print(res) # Output: 1 (300 occurs once in the list)
#universal functions in Python
# my_list=[100,200,300,400,500]
# print(sum(my_list))
# print(min(my_list)) # Output: 100 (smallest element in the list)
# print(max(my_list)) # Output: 500 (largest element in the list)
# import math
# print(math.prod(my_list)) # Output: 12000000000000000000 (product of all elements in the list)
