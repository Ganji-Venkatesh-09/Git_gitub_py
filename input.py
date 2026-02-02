x = 5
y = "venky"
print(x)
print(y)

x = 8
x = "Income"
print(x)

x = str(8)
y = float(4)
z = int(4)
print(x)
print(y)
print(z)

x = 5
y = "Heroo"
print(type(x))
print(type(y))

x = "awesome " #Created var in outside fun 
def myfunc():
    print("Python Is " + x)
myfunc()

x = "Rise East"  #Create outside
def myfunc():
    x = "Rise west" #Create inside with same 
    print("The sun not " + x)
myfunc()
print("The sun " + x)

def myfunc():   #use global keyword variable belongs to the 
    global x
    x = "Keyword variable "
myfunc()
print("Global " + x)

x = "Beginer" #Changes the global variable x from "Beginer" to "Intermediate".
def myfunc():
    global x
    x = "Intermediate"
myfunc()
print("Python " + x)





































