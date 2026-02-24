#loop:loop is a programming structure that repeats a block of code until the given condition is satisfy.
# simple language: it is a programming structure which repeats the block of code whenever specified condition is true.

# It helps in automating repetitive tasks without writing the same code multiple times.
# types of loop
# 1.for: when you know exactly how many times you want to repeat the code eg.counter ie(1 to 10) hami laii tha hunxa kati patak loop run garne vane ra 
    #[list dictionary tuples and range]
    # sanga kaam garna paryo vane we use for loop(rtdl)

# 2.while: when you want to repeat code as long as a condition is true, but you don't know the exact count. eg. logical statement
     #condition ko lagi while loop use garne    
     
# 3.do while :it is same as while loop but it guarantees the code runs at least once before checking the condition
#firstly loop execute and check the condition 
#do while loop python ma use

#for loop:
'''numbers=[1,2,3,4,5]
# print(numbers[0])
# for num in numbers: #for ani eauta variable name and membership operator and define list
#     print(num) #print variable
for i in range(1,10,3): # range is a built_in function to generate the sequence of only numbers first: start 2nd:stop and last: difference or gap
   #why we use the range function: It is highly memory efficient. If you need to loop 1 million times, range(1000000) doesn't store a million numbers
   # in your RAM it just remembers the current number and calculates the next one on the fly. 
 print("the value is",i)
 
# print(list(range(10)))
for x in range(10):
    print("Hello Nepal")'''
        #print even number using for loop
# for x in range(2,10):
#  if x%2==0:
#      print(x)
#      print("Even number")
#  else:
#      print("odd number")
#      print(x)
# total=0
# for x in range(1,10):
#     total+=x
# print(total)

# total=0
# for x in range(1,10):
#     total +=x #left side and right side addition and add on left side ie total=o and x=1 add 1 save on toatl assignment operator
# print(total)


#make the table of 5:
    # for i in range (1,11):
    #     print(f"{13} x {i}= {13 * i}")
  
    
# total=0
# for i in range(1,11):
#     total+=i
# print(total) 

'''for num in range(20):
    num=int(input("enter any number:"))
    if num%2==0:
        print(f"{num} is even number") 
    else:
     print(f'{num} is odd number')
    break'''
    
f