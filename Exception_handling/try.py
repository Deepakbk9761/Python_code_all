# Exception Handling is a programming that manages runtime errors
#The process of handling errors that occur during runtime is called Exception Handling.
# asked to error(magne k error aayo vane ra )
# try:
#  print(10/0)
# except Exception as e:
#     print("Error:",e)
# print("Hello python")


# syntax:
# try:
#     # something logic or code
# except Exception as e:
#     print("Error:",e)


#"This is the error that is passed from us
def div(x,y):
    if y==0:
      raise Exception ("y shouldn't be zero")
    else:
        return x/y
try:
    print(div(10,10))
except Exception as e:
    print("Error:",e)