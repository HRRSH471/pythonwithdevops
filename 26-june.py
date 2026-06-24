# ===============File Handling============
# What is file.?

# Files are store of data and information on the specific path of device

#File handling in python means reading from and writing to files/folder stored on 
#disk using python
# Your python code can open a file , pull out data of it , put data into it and also close it properly

# Types of file
# 1.Text file (.txt , .csv,. json)
# 2.Binary files(images, vedios, audio)

# Types of file path.
# 1 Absolute path: The complete path from the root of the filesystem.
# 2 Relative path : the path relative to where you current folder ()

# file mode
# 1. a : append , a+ : append and read
# 2. w+ : write and read, 
# 3  r+ : read and write
# 4. x  : strictly create file

# python file handling methonds.
# 1.open(file_name,mode): open file
# 2.close() : close file.
# 3.flush() : memory cleanup

# 4.read() : file read
# 5.readlines() : file read line by line
# 6.write() : writes data in file only take string.
# 7 writelines() : write data in file of any data types.

# 8.tail() :cursor move
# 9.seek() :specific position set of cursor

# in-build modules
# os library
# shutil library
# subprocess library
# random library
# string library

#-------------------------------
# create a file
# try:
# file=open("demo.txt","x")
# print("file created")

# except Exception as e :
#     print("Error:",e)

# 1.write mode file creation
file=open("new_demo.txt","w")
file.write("This is file conten using file handling")
print("file created in write mode...")


