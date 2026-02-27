"""
######
#Check whether username is correct AND password is correct.
username =(input("Enter Username: "))
password = (input("Password: "))
if username ==("venky") and password==("123@3.0"):
    print("Login sucessfull")
else:
    print("Lpgin Faild")
########
#Check whether a number is NOT equal to zero.
num = 8
if not (num==0):
    print("number is not equal to zero")

#Check whether a person can enter a club if age is above 18 AND dress code is proper.
age = 25
dress_code = "proper"
if age >18 and dress_code == "proper":
    print("The person can enter a club")
else:
    print("The person can't enter a club")

#Check whether a number is NOT divisible by 2.
num = 10
divisible = 2
if not num % divisible:
    print(True)
else:
    print(False)
 
 #Check whether a person is a child OR a senior citizen.
age = 16
if age <18 or age >=60:
     print("Person is child")
else:
    print("Person is senior citizen")
     
#Check whether a number is between 10 and 50 but NOT equal to 25.
num = 28
if not num==25 and num>10 and num<50:
    print("number is between 10 and 50 but NOT equal to 25")

#Check whether a year is valid if it is greater than 1900 AND less than or equal to current year.
year = 2000
curent_year =2026
if year>1900 and year <= curent_year:
    print("year is valid")
else:
    print("year not valid")

#Check whether a number is either negative OR greater than 100.
num = -10
if num<0 or num>100:
    print("Number is negative")
else:
    print("Number is greater than 0 to 100")
############
#Check whether login is successful if username is correct AND password is correct AND account is active.
username = input("Enter username: ")
password = input("Enter password: ")
msg = "account is active"

if username == "venky" and password == "123" and msg == "account is active":
    print("Login Successful")
else:
    print("Login Failed")
#############
#Check whether a number is divisible by 2 AND divisible by 5.
num =34
if num%2 == 0 and num%5 == 0:
    print("num is divisible by 2 and 5")
else:
    print("num is not divisiblle 2 and 5 ")

#Check whether a person gets discount if age is above 60 OR membership card is valid.
age = 70
membership_status = "valid"
if age>60 or membership_status=="valid":
    print("discount is allowed")
else:
    print("Not allowed")
    
#Check whether a number is NOT between 1 and 10.
num = 11

if not (1 < num < 10):
    print("Number is not between 1 and 10")
else:
    print("Number is between 1 and 10")

#Check whether a triangle is valid if sum of any two sides is greater than the third side.
a = 4
b = 6
c = 7

if a + b > c and a + c > b and b + c > a:
    print("Valid triangle")
else:
    print("Not valid")

#Check whether a number is positive AND NOT divisible by 3.
num = 6

if num > 0 and num % 3 != 0:
    print("Both are true")
else:
    print("Both are not true")

#Check whether exam result is distinction if marks are above 75 AND attendance is above 90%.
marks = 85 
attendence = 0.90
if marks>75 and attendence>=0.90:
    print("Distinction")
else:
    print("Not Distinction")
"""
#🔗 LOGICAL OPERATORS - PRACTICE PROBLEMS...............
#'''''''''''deepseek

#Check if a person is allowed to watch an adult movie (age must be 18 or above AND must have parent permission).
age = 18
permisson = "parent acepted"
if age>=18 and permisson=="parent acepted":
    print("Person is allowed ")
else:
    print("Person is not allowed")

#Student gets scholarship if marks > 85 OR family income < 50000.
student_marks = 85
family_income =60000
if student_marks>85 or family_income<50000:
    print("sStudent is eligible for scholorship")
else:
    print("Student is not eligible for scholorship")

#Given a boolean (True/False), print its opposite.
# Version 1: Your original logic (condition is False)
person1 = True
person2 = False
if not person1 and person2:
    print("This will NEVER print")
else:
    print("This will ALWAYS print because condition is False")

#Check if today is a holiday OR weekend to decide if you can sleep late.
day = "sunday"
weekend = "saturday"
holiday = True
if day =="sunday" or weekend=="saturday" or holiday==True:
    print("Late sleepe")
else:
    print("Wake up early")

#Person can get license if age >= 18 AND passed test AND NOT having medical ban.
age = 18
test = "passed test"
medical = "No medical restriction"
if age>=18 and test=="passed test" and medical=="No medical restriction":
    print("The person is eligible")
else:
    print("Not eligible")

#Check if a letter is vowel (a, e, i, o, u) OR consonant.
letter = "a"
if letter in "aeiou":
    print("Vowel")
else:
    print("Consonant")

#Customer gets discount if they are senior citizen (age >= 60) OR student with valid ID.
senior_citizen =60
student ="valid Id"
if senior_citizen>=60 or student=="valid Id":
    print("get discount")
else:
    print("No discount")

#Take three side lengths. To be a valid triangle, all three conditions must be true:
a = 4
b= 6
c = 8
if a+b>c and b+c>a and c+a>b:
    print("form Triangle")
else:
    print("Not")

"""Withdraw money allowed if:

Amount ≤ balance AND

Amount is multiple of 100 AND

NOT (amount > daily_limit)
"""
ammount = 5000
balance= 5000
multiple =ammount*100
daily_limit =4000
if ammount<=balance and ammount %100==0 and ammount<=daily_limit:
    print("withdraw money allowed ")
else:
    print("No")

#🧠 LOGICAL OPERATORS TEST (Level 1 → Easy + Medium)

#Question 1Check whether a number is: Greater than 10 AND Less than 50
number = 25
if number >10 and number <50:
    print("True")
else:
    print("False")

"""
Question 2
Check whether a number is:
Even
OR
Divisible by 5
"""
number = 26
if number or number/5:
    print("Even")
else:
    print("Divisible")

"""
Question 3
Allow login if:
Username is "admin"
AND
Password is "1234"
AND
Account is active (True)
"""
Username ="admin"
Password ="1234"
account_is_active =True
if Username=="admin" and Password=="1234" and account_is_active:
    print("Allow")
else:
    print("Not Allow")

"""
Question 4
Check whether a number is:
NOT negative
AND
NOT equal to 0
"""
number = 20
if not number<0 and not number==0:
    print("True")
else:
    print("False")

    """
    Question 5 (Thinking Question 🔥)
A person gets bonus if:
Salary > 30000
OR
Experience > 5 years
BUT
NOT under disciplinary action (False)
    """
salary = 35000
experience = 6
under_disciplinary_action =False
if salary>30000 or experience>5 and not under_disciplinary_action:
    print("Person gets bonus")
else:
    print("Person not gets bonus")

#🧠 LEVEL 2 TEST
"""
Question 1
A number is special if:
It is divisible by 3
AND
NOT divisible by 5
"""
number = 6
if number%3==0 and not number%5==0:
    print("True")
else:
    print("False")

    """
    Question 2

A student passes if:
Marks ≥ 40
AND
Attendance ≥ 75%
OR
Has medical certificate (True)
    """
marks = 40
attendance =0.75
medical_certificate =True
if marks>=40 and attendance>=0.75 or medical_certificate:
    print("Student Pass")    
else:
    print("Student Not pass")

    """
    Question 3
Access granted if:
User role is "admin"
OR
(User role is "editor" AND account verified is True)
    """
user_role = "admin"
user_role = "editor"
account_verified = True
if user_role=="admin" or user_role=="editor" and account_verified:
    print("access granted")
else:
    print("Access not granted")

    """
    Question 4
A loan is approved if:
Salary > 25000
AND
Credit score > 700
AND
NOT blacklisted
    """
salary = 30000
credit_score =720
blaclist = True
if salary>25000 and credit_score>700 and not blaclist:
    print("Loan Approved")
else:
    print("Loan not approved")

    """
    Question 5 🔥 (Hardest) A person is eligible for promotion if:
Experience ≥ 5 years AND
Performance rating ≥ 4 OR
Completed special project BUT
NOT under warning
⚠ This one requires correct grouping.
    """
experience = 5
performance_rating = 4
special_project ="Completed"
not_under_warning = True
if experience>=5 and performance_rating>=4 or special_project=='Completed' and not not_under_warning:
    print("Eligible for pramotion")
else:
    print("Not eligible for pramotion")




















