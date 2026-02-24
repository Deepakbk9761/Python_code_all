# keyword argument is also called named argument or dictionary argument :it maximal use with dictionary
# **kwargs 
# suntax:
# def function_name(*args,**kwargs):
#     print(args)
#     print(kwargs)
# function_name(25,35,65)   

# eg:
def users(*args,**kwargs):
    print(args)
    print(kwargs)
users('ram','sita',name='deepak',age=36) #key value pair form data should we enter name='deepak',age=36 ie placed on dictionary form 'ram','sita' tuples