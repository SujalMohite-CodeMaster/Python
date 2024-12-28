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

# Some other methods
letters = list("My name is 'Sujal Mohite'")
#if i want to print the every elemnet in string i can use 
print(letters)

# methods in list

num_list.append(90)
print(num_list)

num_list.extend(var)
print(num_list)

num_list.remove("D")
print(num_list)

print(num_list.sort)

# Operation on list
num = [2,4,3.4,54,34,56,32]
print(max(num))
print(min(num))
print(sum(num))
avg = sum(num)/len(num)
print(avg)