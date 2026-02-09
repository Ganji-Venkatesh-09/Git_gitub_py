

##Calculate the area of a triangle using Heron's formula.

#Add two numbers and display the result
num1 = 756
num2 = 8474
print(num1+num2)

#Subtract one number from another number.
sub = num2 - num1
print(sub)  

#Multiply two numbers and print the result.
mul = num1 * num2
print(mul)

#Divide one number by another number.
div = num1 / num2 
print(div)

#Find the remainder when one number is divided by another.
rem = num2 % num1 
print(rem)

#Find the power of a number.
power = num1 ** 2
print(power)

#Perform floor division on two numbers.
floor = num2 // num1 
print(floor)

#Calculate the total of three numbers.
num3 = 7847
total = num1 + num2 + num3 
print(total)

#Find the difference between the largest and smallest of two numbers.
largest = num2 - num1 
print(largest)
smalest = num1 - num2
print(smalest)
diffrence = largest - smalest
print(diffrence)  

#Divide two numbers and find both quotient and remainder.
div = num1 / num2 
print(div)
rem = num2 % num1
print(rem)

#10.......................

#Calculate the average of two numbers.
ave1 = 45
ave2 = 89
calc = ave1 + ave2
average = calc / 2
print(average)

#Find the square of a number.vvvv
sq_num = 76
square = sq_num ** 2
print(square)

#Find the cube of a number.
cube_num = 6
cube = cube_num ** 3
print(cube)

#Calculate total marks of 5 subjects.
sub1 = 73
sub2 = 89
sub3 = 65
sub4 = 54
sub5 = 89
total_marks = sub1 + sub2 + sub3 + sub4 + sub5 
print(total_marks)
"""
sub1 = int(input("Enter marks of subject 1:"))
sub2 = int(input("Enter marks of subject 2:"))
sub3 = int(input("Enter marks of subject 3:"))
sub4 = int(input("Enter marks of subject 4:"))
sub5 = int(input("Enter marks of subject 5:"))
total = sub1 + sub2 + sub3 + sub4 + sub5
print("Total marks: ", total)
"""
#Calculate remaining amount after spending money.
total_ammount = 1000
spending_ammount = 270
remaining_ammount = total_ammount - spending_ammount
print(remaining_ammount)

#Calculate remaining amount after spending money.
many_items = 27
same_price = 360
total_price = many_items * same_price
print(total_price)

#Divide total chocolates equally among children.
total_choco = 475
total_child = 256
divide = total_choco / total_child
print(divide)

#Find how many items remain after equal distribution.
total_items = 987
equal_distribution = 6
remain_item = total_items % equal_distribution
print(remain_item)

#Find the result of a number raised to power zero.
number = 45 
print(number ** 0)

#Find the floor value after dividing two numbers.
#First method 
first_num = 24
second_num = 87
divide_two_num = first_num / second_num 
floore_value = int(divide_two_num)
print(floore_value)

#second method 
first = 98
second = 43
floor_value = first // second 
print(floor_value)

#DeepSeek ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

#Create a program that calculates the sum, difference, product, and quotient of two numbers.
number_a = 36
number_b =83
Cal_Sum = number_a + number_b
Cal_Diff = number_a - number_b 
Cal_Prod = number_a * number_b #Multiplication
Cal_Quot = number_a / number_b  #Division   
print(Cal_Sum,Cal_Diff,Cal_Prod,Cal_Quot)

#Calculate the area of a rectangle and a circle.

#For rectangle Formula is Area = Length * Bridth
Length = 29
Bridth = 14
Area_Rectangle = Length * Bridth 
print("Area of rectangle is: ", Area_Rectangle)

#For circle Formula is Area = pi * radius ** 2
radius = 9
pi = 6.26
Area_Circle = pi * radius ** 2
print("Area of circle is : ",Area_Circle)

#Find the remainder when dividing two numbers and check if a number is even or odd.
num1 = 87
num2 = 56
remainder = num1 % num2 
print("Remainder is: ", remainder)
number3 = 46
if number3 % 2 == 0:
    print("The number is even.")
else:    
    print("The number is odd.")

#Calculate power (exponent) and floor division (how many whole times it divides).
base = 7
exponent = 4
power_result = base ** exponent
print("power is: ", power_result)

floor_num1 = 67
floor_num2 = 54
floor_division_result = floor_num1 // floor_num2    
print("Floor Division Result Is :", floor_division_result)

#Calculate: (a² + b²) / (a - b) + (a % b)
a = 4
b = 6
a_square = a ** 2
b_square = b ** 2
sum_of_a_b_squares = a_square + b_square 

a_b_subtract = a - b

division = sum_of_a_b_squares / a_b_subtract 

module_of_a_b = a % b 
final_result = division + module_of_a_b
print("Final Result Is: ", final_result)

#Convert Celsius to Fahrenheit using formula: F = (C × 9/5) + 32
celsius = 76
fathrenheit = (celsius * 9/5) + 32
print("Fathrenheit is: ", fathrenheit)


#Calculate total bill with discount and tax:
#Total = (Price × Quantity) - Discount + Tax
price = 499
quantity = 20
discount = 40
tax = 19
total = (price * quantity) - discount + tax
print("total bill with discount and tax: ", total)

#Calculate exact age in years, months, and days from total days lived.
total_days = 1000
years = total_days //365
remaining_after_years = total_days %365
months = remaining_after_years // 30
days = remaining_after_years % 30
print("Years: ", years)
print("Months: ", months)
print("Days: ", days)

#
x = 5
y = 3
z = 8
average = x + y + z / 3 
'''#Find the largest 
largest = x
if y> largest:
    largest = y
if z > largest:
    largest = z 

smallest = x
if y < smallest:
    smallest = y 
    if z < smallest:
        smallest = z 
print("Average; ",average )
print("Largest", largest)
print("Smallest", smallest)
'''
Largest = max(x,y,z)
Smallest = min(x,y,z)
print("Average; ",average )
print("Largest", Largest)
print("Smallest", Smallest)

#Calculate the volume of a cube and a sphere.
#Volume of cube = side³
side = 3
volume_cube = side ** 3
print("Volume of cube is: ", volume_cube)

#Volume of sphere = 4/3 * pi * radius³
radius = 6
pi = 16.4
volume_sphere = (4/3) * pi * radius ** 3
print("Volume of sphere is: ", volume_sphere)





