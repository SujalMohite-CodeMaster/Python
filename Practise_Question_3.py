#Take a user input and print the following pattern
"""
1
12
123
1234
12345
"""



m = int(input("Enter the number "))

for i in range(1,m+1):
    for j in range(1,i+1):
        print(j,end="")
    print()
        
'''
*****
*****
*****
*****
*****
'''

for i in range(5):
    for j in range(5):
        print("*", end="")
    print()

'''
*****
*   *
*   *
*   *
*****
'''
n = 5
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or j==1 or i==n or j==n :
            print("*",end="")
        else:
            print(" ",end="")
    print()


'''
*
**
***
****
*****
'''
n=5
star = "*"
for i in range(1,n+1):
    for j in range(1,n+1):
        if i>=j:
            print(star,end="")
    print()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     

"""
*****
****
***
**
*
"""

n=5
for i in range(1,n+1):
    for j in range (1,n+1):
        if i<=j:
            print("*",end="")
    print()

"""
1
13
135
1357
13579
246810
2468
246
24
2
"""

#Nested for loop for upper odd number triangle
for i in range(1,11,2):
    for j in range(1,i+1):
        if i%2!=0 and j%2!=0:
            print(j,end="")
    print()

#Nested for loop for lower even number triangle.

for i in range (5,0,-1):
    for j in range(1,i+1):
    
        print(j*2,end="")
    print()

"""
00000000010
000000009
00000008
0000007
000006
00005
0004
003
02
1 
"""
n=10
for i in range(n):
    for j in range(n-i-1):
        print("0",end="")
    print(n-i)