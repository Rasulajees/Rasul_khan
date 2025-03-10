"""
#using name:

my_string= "Rasul khan"
x=1
for i in my_string:
    print(my_string[0:x]) 
    x=x+1
#--------------------------
#using python:

my_string="python"
word="python"
for letter in word:
    print(letter)

#--------------------------
#right angle triangle

n=7
for i in range(1,n+1):
    print("*"*i)

#--------------------------
#square traingle:

n=5
for i in range(n):
    print("*"*n)

#--------------------------
# while loop:

n=5
i=0
while i<=n:
    print(i*"*")
    i+=1

#--------------------------
#left hand triangle:

n=6
for i in range(n):
    print(" "*(n-i)+"*"*i)
"""
#--------------------------
#dimanded triangle:

n=6
for i in range(n):
    print(" "*(n-i)+"*"*(2*i+1))

#--------------------------
"""
#bardered square

n=5
for i in range(n):
    if i==0 or i==n-1:
        print("*"*n)
    else:
        print("*"+" "*(n-2)+"*")

#--------------------------

"""
#daimond:
"""
n=6
for i in range(n):
    print(" "*(n-i)+""*i+("*"*i))
for j in range(n,0,-1):
        print(" "*(n-j)+""*i+("*"*j))    
"""