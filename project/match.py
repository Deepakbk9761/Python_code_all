#Match is the statement takes an expression and compares it successively values using case blocks:
#it checks not only data it also checks structure  of data how to make
#in last of we use case_(underscores)
#Note: if else ko satta ma match ani case use garxau in simple


'''language = "Nepali"

match language:
    case "Nepali":
        print("Your language is Nepali")
    case "English":
        print("Your language may be English")
    case "Chinese":
        print("Your language is chinese")
    case _:
        print("Not found your language")'''

#swap a value
'''x=10
y=20
x=x+y
y=x-y
x=x-y
print(x)
print(y)
# or
y=y-x
x=x+y'''

#Ascending order Number
'''x=10
y=20
z=30
if x>y and x>z:
    if y>z:
        print(x,y,z)
    else:
        print(x,z,y)

elif y>z and y>x:
    if z>x:
        print(y,z,x)
    else:
        print(y,x,z)
else:
    print(z,y,x)'''
    
users=[
    {'user_name':"Deepak",'age':12,'password':12345},
    {'user_name':"sita",'age':12,'password':2345}
        
    ]


# print(users[0]['user_name'])
if users[0]['user_name']=='Deepak' and users[0]['password']==12345:
 print("Login Successful!",users[0]['user_name'])
elif users[1]['user_name']=='sita'and users[1]['password']==2345:
 print("Login successful",users[1]['user_name'])
else:
    print("invalid password")
