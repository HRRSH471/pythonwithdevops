start_point = int(input("Enter the start point: "))
end_point = int(input("Enter the end point: "))   
for i in range(start_point, end_point + 1):
    if i % 2 == 0 and i % 3 == 0:
        print(i, end=" ")  