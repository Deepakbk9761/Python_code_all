# there is two types of file:
#     Binary file:which can't be possible to change like image address
#     text file: it can be changable
# crud operation: create read update delete
# w -> "Write " 
# r -> "read"
# a -> "appened"
name=input("Enter your Name:")
age=input("Enter age:")
address=input("Enter address:")
mail = input("Enter email: ")

handle=open("file_handling/Record.txt","a") #that creates the txt.file
handle.write(f"My name is {name} and i am {age} years old. Recently my address is {address} and email is {mail}")  
handle.write("\n")
handle.close()
