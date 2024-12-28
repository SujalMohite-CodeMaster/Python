num_list = [1,8,5,4,56,89,21,56,75,6,45,42]

print(num_list)
print(len(num_list))

var = ["A","B","C","D","Sujal","Mohite"]

print(var)
print(type(var))

# concate the lists

mix = num_list + var
print(mix)

#Extract the elements of the list
print(num_list[:12])

print(num_list[0:])

print(num_list[5:11])

print(var[-1:-4])

print(var[::-1])#this is usedto print the list in reverse order

print(num_list[2:10:2])# this will print the every second element of list in a range of 2 to 10
