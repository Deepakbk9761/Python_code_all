# function: Resusable block of code that is used to perform a single related action.
# A function works in three step:
#1.Defining: to create a function using "def" keyword def=define or predefine word
#2. Calling: The code inside the function doesn't run until you "call" it by its name.
#3.Returning (Optional): The function can send a result back to you.

# syntax:

'''def function_name(parameter): function defn
    # code
    return
    function_name(argument) function call
    
def total(x,y):
    print (x+y)
total(10,20)

def difference(x,y):
    print(f"The difference of {x} and {y} is:",x-y)
difference(20,10)
difference(100,99.8)

def mul (x,y):
    print(x*y)
mul(10,10)


def div(x,y):
    print(x/y)
    
div(5,2)

def message (No_of_users):
    for i in range(No_of_users):
        print("Hello dear")
message(5)
# wap to determine the even or odd number using function
def number(x):
    if x%2==0:
        print(f" Your number {x} is Even")
    else:
        print("odd number")
number(10)
# multiplication table in python code using function
def mul(x): #define the multiple  
    for i in range(1,11):
     print(f"{x} x {i}={x*i}")
     print(x)
n=int(input("Enter the number:"))  
mul(n)
mul(n)

# Division table in python
def num(x):
    print(x)
    for i in range(1,11):
     print(f"{x} /{i}={x/i}")
n=int(input("Enter the number:"))  
num(n)
#WAP that takes user information and displays it using f-strings for clean formatting.
def user_info(name,email,address):
    print(f"My name is {name}")
    print(f"my email is {email}")
    print(f"my address is {address}")
x=input(f"Enter your Name:")
y=input("enter your email:")
z=input("enter your address:")
user_info(x,y,z)

#WAP to create a function named calculate_area that takes length
#and breadth as input from the user and prints the area of a rectangle.
def calculate_area(L,B):
    Z=L*B
    print("The Area of Rectangle is:",Z)
x=int(input("Enter the length:"))
y=int(input("Enter the Breadth :"))
calculate_area(x,y)

#WAP to define a function check_voter that takes name and age as parameters.
# If the age is 18 or older, print "[Name] is eligible to vote." Otherwise, print "[Name] is not eligible."
def check_voter(name,age):
    age=18
    if age>=18:
        print(name,"is eligible to vote")
    else:
        print(name,"is not eligible to vote")
name=input("Enter your name:")
age=int(input("Enter your age:")) 
check_voter(name,age)'''

# 

'''users=[
    {'name':'Deepak','gender':"male","status":'true'},
    {'name':'ram','gender':"male","status":'false'},
    {'name':'gita','gender':"female","status":'true'},
    {'name':'sarada','gender':"female","status":'true'},
    {'name':'gopal','gender':"male","status":'true'},
    {'name':'sarita','gender':"female","status":'false'},   
    {'name':'Manisha','gender':"female","status":'true'},
]
total_user=len(users)
total_male=0
total_female=0
total_active_male=0
total_inactive_male=0
total_active_female=0
total_inactive_female=0
for user in users:
    if user['gender']=='male':
        total_male+=1 #count total male
        if user['status']=='true':
            total_active_male+=1
        else:
            total_inactive_male+=1
       
    else:
        total_female+=1 #count total female
        if user['status']=='true':
            total_active_female+=1
        else:
            total_inactive_female+=1
            
print(f'total user:{total_user}')
print(f'total male:{total_male}')
print(f'total female:{total_female}')
print(f'total active_male:{total_active_male}')
print(f'total inactivemale:{total_inactive_male}')
print(f'total activefemale:{total_active_female}')
print(f'total inactivefemale:{total_inactive_female}')'''


