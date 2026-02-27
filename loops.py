""" 
🔹 Problem 1 – Basic Counter
Print numbers from 1 to 20 using while loop.
"""
num =1
while num <=20:
    print(num)
    num +=1

""" 
🔹 Problem 2 – Even Numbers Only
Print even numbers from 1 to 50.
"""
num=2
while num<=50:
    print(num)
    num+=2

""" 
🔹 Problem 3 – Reverse Counting
Print numbers from 20 down to 1.
"""
num=20
while num>=1:
    print(num)
    num-=1

# 1️⃣ Print Range (Basic Counter Control)
# Print numbers from 1 to 10
i=1 #intilize
while i<=10: #condition
    print(i) #work
    i+=1 #update

# Print numbers from 5 to 15
i=5 #Intiliz
while i<15: #Condition
    print(i) #work
    i+=1 #Update
    
# Print numbers from 1 to n (take n from user)
n=int(input("Enter n:"))  #inputof n
i=1 #intilize
while i<=n: #condition
    print(i)  #work
    i+=1     #updatee
    
# Print numbers from n to 1 (reverse using user input)
n=int(input("Enter n:"))   #intilize
i=1  # normally taken variablename
while n>=i: #condition
    print(n)  #work
    n-=1     #updatee
    
# Print numbers from -5 to 5
i=-5  #intilize
while i<=5: #condition
    print(i)  #work
    i+=1 #update
# 2️⃣ Reverse Range (Control Direction)
# Print numbers from 10 to 1
i=10  #Intilize
while i>=1:    #Condition 
    print(i)    #work
    i-=1    #update
    
# Print numbers from 20 to 5
i=20  #Intilize
while i>=5:    #Condition 
    print(i)    #work
    i-=1    #update

# Print numbers from n to 0
n=int(input("nter n:")) #intilize
while n>=0:   #Condition
    print(n)   #Work
    n-=1   #Update
    
# Print numbers from 100 to 50
i=100  #intilize
while i>=50:  #condition
    print(i)   #work
    i-=1    #update
    
# Print numbers from 50 to 100 (careful with direction)
i=50  #intilize
while i<=100:   #Condition
    print(i)    #work
    i+=1   #Update

# 3️⃣ Sum Range (Accumulator Practice)
# Find sum of numbers from 1 to 10
i=1   # Intilize
total=0  #Intilize Acumulator
while i<=10:   #Condition
    total+=i   # Work main logic 
    i+=1   # Update
print("Sum =", total)  # Final work

# Find sum from 1 to n
i=1
n=int(input("Enter n:"))
total=0 
while i<=n:
    total+=i
    i+=1
print("Sum =",total)

# Find sum from 10 to 20
i=10
total=0
while i<=20:
    total+=i
    i+=1
print("Sum =",total)

# Find sum of numbers from n to m (both user input)
n = int(input("Enter n:"))
m = int(input("Enter m:"))
total = 0
if n <= m:
    while n <=m:
        total+=n
        n+=1
else:
    while n>=m:
        total+=n
        n-=1
print("Sum =",total)

# Find sum of first n natural numbers
n=int(input("Enter n:"))
total=0
i=1
while i<=n:
    total+=i
    i+=1
print("Sum=",total)

# 4️⃣ Conditional Sum (Loop + If Mixing)
# Find sum of even numbers from 1 to 20
i=2
total=0
if i<=20:
    while i<=20:
        total+=i
        i+=2
print("Sum=",total)

# Find sum of odd numbers from 1 to 20
i=1
total=0
if i<=20:
    while i<=20:
        total+=i
        i+=2
print("Sum=",total)
# Find sum of even numbers from 1 to n
n=int(input("Enter n:"))
i=1
total=0
if i<=n:
    while i<=n:
        total+=i
        i+=1
print("Sum=",total)

# Find sum of numbers divisible by 3 from 1 to 30
i = 1
total = 0
while i <= 30:
    if i % 3 == 0:     # divisible check
        total += i    # add the number
    i += 1            # update
print("Sum =", total)

# Find sum of numbers divisible by 5 between 10 and 50
i = 10
total = 0
while i <= 50:
    if i % 5 == 0:     # divisible check
        total += i    # add the number
    i += 1            # update
print("Sum =", total)


