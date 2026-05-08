# Loops in python
# for loop : ranged based
# While loop : Condition based
# for loop is used when we know the number of iterations in advance. It is used to iterate over a sequence (like a list, tuple, string) or other iterable objects. The syntax of a for loop is:
# for variable in sequence:
# range() function is used to generate a sequence of numbers. It takes three arguments: start, stop, and step. The start argument is the starting number of the sequence (default is 0), the stop argument is the ending number of the sequence (exclusive), and the step argument is the increment between each number in the sequence (default is 1). The syntax of the range() function is:
# range(start:0, stop-1, step:1)

# for i in range(0, 10, 2):  
#     print(i, end=" ")  # Output: 0 2 4 6 8 # end=" " is used to print the output in the same line with a space in between. If we don't use end=" ", the output will be printed in a new line for each iteration.
# for i in range(1,21):
#  if i%2 !=0:
#     print(f"{i} is odd number")
#  else:
#    print(f"{i} is even number")

# s=0
# for i in range(1,5):
#     s=s+i  
# print(s)   
# for r in range (10, 11,-1):
#     print(r, end=" ") 
# for i in range(1, 11):
    # if i ==6:
        # continue      # continue statement is used to skip the current iteration and move to the next iteration. In this case, when i is equal to 6, the loop will skip the print statement and move to the next iteration.
    # print(i, end=" ")  # Output: 1 2 3 4 5 7 8 9 10

  # 1. Write a program to takes start point and end point from user input and print all number divisible by 2 and 3

start_point = int(input("Enter the start point: "))
end_point = int(input("Enter the end point: "))
if end_point > start_point:
    if end_point==start_point:
        print("Start point and end point are the same. No numbers to check.")
    else:    
     for i in range(start_point, end_point + 1):
        if i % 2 == 0 and i % 3 == 0:
            print(i, end=" ")
else:
    print("Invalid input: End point should be greater than start point.")

  # ....2.Write a program to take a number from user input and print formated table..............
# num = int(input("Enter a number: "))
# for i in range(1, 11):
#     print(f"{num} x {i} = {num * i}")
 # Wap to take a number from user input and print formated table in reverse.
# num = int(input("Enter a number: "))
# for i in range(10,0, -1):
#     print(f"{num} x {i} = {num * i}")
