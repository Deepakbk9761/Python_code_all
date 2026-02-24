# student=[] #variable declair
# num=int(input("Enter the number of students:")) #take input from user
# for i in range(num): 
#     name=input("Enter the name of students:")
#     student.append(name)  
# print(student)

#WAP to take the number of values from user  and calculate sum of all values
# total=0
# num=int(input("Enter the Data:"))
# for i in range(num):
#     take=int(input("Enter the number:"))
# print("Your total is Rs",total)



'''number=[]
num=int(input("Enter the number of data:"))
for i in range(num):
    take=int(input("enter your number:"))
    number.append(take)
print(number)


#student result prepare:
num=int(input("Enter the number of sudent:")) #take input from the user where num is variable
x=1 #This is a counter variable that starts the count from the first student.
total_marks=[] #This is an empty list used to store the final calculated marks of each student.
while x<num:   #This is a loop that repeats the process as long as x is less than num 
    print(f"=======student:{x}========")
    for i in range(1): #Execute the code inside this loop exactly 1 time.
        nep=int(input("enter your Nepali Marks:"))
        math=int(input("enter your math marks:"))
        social=int(input("enter your social marks:"))
        English=int(input("enter your English marks:"))
        c_programming=int(input("enter your c_programmin marks:"))
        Microprocessor=int(input("enter your Microprocessor marks:"))
        stat=int(input("enter your  stat marks:"))
        total=nep+math+social+English+c_programming+Microprocessor+stat
        total_marks.append(total)
    x+=1 #This increments the counter by 1, moving the process to the next student
   
for total in total_marks:
    per=total/7
    Grade=""
    if per>35 and per<=45:
       Grade="C"
    elif per>45 and per<=55:
         Grade="C+"
    elif per>55 and per<=65:
         Grade="B"
    elif per>65 and per<=75:
         Grade="B+"
    elif per>75 and per<=85:
         Grade="A"
    elif per>85 and per<=100:
         Grade="A+"
    else:
        print("Fail No grade")
    print(f"total marks:{total_marks},Percentage:{per}, Grade:{Grade}")'''
    
'''Right angle triangle
*
**
***
****
*****
for i in range(1,6):#outer loop that controls the Rows
    for j in range(i):#inner loop that controls the Columns if i =1 ,j=[0] and i=2 ,j will[0,1]
     print("*",end="")
    print()# that pressing the Enter key on your keyboard. it help to move the cursor in next line
    
#left angle tringle
*****
****
***
**
*
for i in range(5,0,-1):
    for j in range(i):
        print('*',end="")   
    print()
   
#print 1,2,3,4,5 ie forward counting
1
12
123
1234
12345
for i in range(0,6,1):
    for j in range(i):
        print(j+1,end='') #print j+1
    print()

1
22
333
4444
55555
for i in range(1,6):#
    for j in range(i):here already 1 print 
                      #move into the next line and move
        print(i,end='') #also print i ie 2 in above and here also print2 ie 22
    print()
#Backward counting  
12345
1234
123
12
1

for i in range(5,1,-1):
    for j in range(i):
        print(j+1,end="") # j always start from 1 and increase by 1
    print()
#Backward counter using function
def backward_counter(x,y):
 for i in range(x,y,-1):
    for j in range(i):
        print(j+1,end="") # j always start from 1 and increase by 1
    print()
a=int(input("Enter a number:"))
b=int(input("Enter another number:"))
backward_counter(a,b)

#write a code to print this pattern:
1
01
101
0101
10101

for i in range(1,6):
 for j in range(1,i+1):
     if (i+j)%2==0:
        print(1,end="")
     else:
      print(0, end=" ")
 print()
'''  