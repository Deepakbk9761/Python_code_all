'''User-Defined Function: It is a named block of code created by the programmer to perform a specific action.
It helps in making the code organized, reusable, and easy to read.


def function_name(parameters): # def is a keyword used to start the function header.,function_name: A unique name to identify the function.
    # Doc_string (Optional)  (:)) Marks the end of the function header.
    # Block of code (Logic)
    return value # Optional
    
1.#define function
    def introduction():
    #function body
        print("I am a intro function")
 #function call
introduction()

2.function with parameters
def my_intro(name):
    print(f"Your name is {name}")
x=input("Enter your name:")
my_intro(x)

3.optional parameters/default parameters
An optional parameter is a parameter that has a default value assigned to it in the function definition.
If the caller does not provide a value for that argument, the default value is used.  
eg.def my_intro(name="Deepak",age=20):
    print(name,age)
my_intro()

'''
# def users(name):
#     print(name) 
# users(['ram','shyam','hari'])  #but we don't use like users('ram', 'shyam', 'hari') because we initalize one parameter and send three argument