#IF ELSE ELIF AND NESTED IF ELSE


# if condition: it is used to check the condition and execute a block of code if condition is true

'''x=7
y=7
if x>y:
    print("x is greater than y")
elif x==y:
    print("x and y are equal")
else:
    print("x is less than y")

age=19
if age>18:
    print("Age is eligible for voting")
elif age<18:
    print("age is not eligible for voting")
else:
    print("age can do both either voting or not")'''


'''x=7
y=8
z=9
if x>y and x>z:
    print("x is greater than y")
elif x==y and x==z:
    print("x, y and z are equal")
elif y>z and y>x:
    print("y is greater then x")
else:
    print("y is less than z but x is greater than y")'''

#student result print
'''english=int(input("Enter the marks of english:"))
math=int(input("Enter the marks of math:"))
science=int(input("Enter the marks of science:"))
nepali=int(input("Enter the marks of nepali:"))
total=english+math+science+nepali
print("the total  marks is:",total)
percentage=(total/5)
print("your percentage is:",percentage)
if percentage>=90:
    print("Grade A+")
elif percentage>=80 and percentage<90:
    print("Grade A")
elif percentage>=70 and percentage<80:
    print("Grade B+")
elif percentage>=60 and percentage<70:
    print("Grade c")
elif percentage>=50 and percentage<60:
    print("Grade d")
else:
    print("D+")'''
'''marks=int(input("Enter your marks:"))
if marks>=90:
    print("you have to success to get A+ in all")
elif marks>=80:
    print("you have to success to get B+ in all")
elif marks>=70:
    print("you have to success to get C+ in all")
elif marks>=60:
    print("you have to success to get c in all")
elif marks>=29:
    print("you have to success to get d in all")
else:
    print("you are fail")'''

# make the calculator using python code
print("1.Add")
print("2.subtract")
print("3.Multiply")
print("4.Divide")

x=int(input("Enter the first number:"))
y=int(input("Enter the second number:"))
num=int(input("enter your choice between 1 to 4:"))
if num==1:
    print(x+y)
elif num==2:
    print(x-y)
elif(num==3):
    print(  x*y)
elif num==4:
    print("your answer is:",x/y)
else:
    print("invalid choice")


#wap to check whether the number is even or odd
num1=float(input("enter the first number:"))
# num2=int(input("enter the second number:"))
if num1%2==0:
    print("your number is even")
elif num1%2==1:
    print("your number is odd")
else:
    print("This is a decimal number, not a perfect even or odd integer.")

#wap to enter any number and check whether it divisible by 3 and 5
num=float(input("enter the number:"))
if num%5==0 and num%3==0:
    print(f"{num} is divisible by 3 and 5")
else:
    print(f"{num} is not divisible by 3 and 5")

#wap to enter a year and chek whether leap year or not
int=int(input("enter the year:"))
if int%4==0:
    print(f"{int} is leap year")
else:
    print(f"{int} is not leap year")


#wap to check this number is positive or negative

num=float(input("Enter the number:"))
if num<=0:
    print(f"{num} is negative number")
else:
    print(f"{num} is positive number")
