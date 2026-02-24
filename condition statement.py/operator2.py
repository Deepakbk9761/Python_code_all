# Operators
# 1.Arithmetic operators like: +,-,*,%, **,//
# %= modulus : to check the reminder value 
# ** exponential
# // float division
'''print(2%5)
print(2**3)
print(4**4) 

print(19//4)
'''

# assignment operator:=, +=, -=, *=, /=,same as arithmetic operator
'''a=6
a+=79
print(a)
'''
# comparison operator:==, !=, >, <, >=, <=
'''a=6
b=7
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
'''
# logical operator: mainly use in if else condition
# and : return true if both statement is true
# or : return true if one of the statement is true
# not : reverse the result, return false if the result occurs true
'''a = 6
b = 7

if a > b:
 print("True")  #indented space need
else:
    print("false") # Indented 4 spaces

    print(5<3 and 5>3)
    print(5>3 or 5>6)
    print(not(5>3 and 5<4))
'''
    # identity operator
    # is: return true if both variable are the same object
    # is not: return true if both varibles are not same
'''a=4
    b=6
    c=a
    print(a is not b)
    print(a is not c)
    print( b is not c)'''
     

    #membership operator : kunai pane word xa ke xaina in question ma vane ra check garna use hunxa
    # in : return true if a sequence with the specified value is present    in the object :
    # notin : return true if a sequence with the specified value is not present in the object
name="Deepak"
print("D" in name)



    # Bit wise operator: always in binary number system
# &, |, ^, ~, <<, >>
    