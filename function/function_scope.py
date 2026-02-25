'''function scope 
1.Local scope
A varible created inside the function.
It only exists while the function is running
we cannot access a local variable from outside its function.
Local variable'''
def greet():
    name="Deepak"
    print("Namaste", name) #Access global varible inside the function
greet()

'''2. Global scope
 A variable created outside the function'''
name="Deepak"#global variable
def greet():
    print("Namaste", name) #Access global varible inside the function
greet()

# eg.exceptional case:
a=6
def num():
    global a # we define global varible here
    a=a+5
    print(a)


num()
print(a)
a=6
def add():
    b=a+6
    print("the value is:",b)
add()
print(a)


#make a calculator which calculate the simple interested using function in python
def take_value():
  p=int(input("Enter your principal amount:"))
  t=int(input("Enter your time in year:"))
  r=int(input("Enter your Rate:"))
  return [p,t,r]

def calculate():
    p,t,r=take_value()
    return p*t*r/100
def display():
    print("simple intresed is:",calculate())
display()




